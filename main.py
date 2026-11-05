import sys
from modules.service_manager import ServiceManager
from modules.program_manager import ProgramManager
from modules.inquiry_manager import InquiryManager
from modules.search_filter import (
    search_services,
    filter_services,
    search_programs,
    filter_programs,
    search_inquiries,
    filter_inquiries,
    universal_search
)
from modules.reports import (
    print_business_report,
    get_services_by_category,
    get_programs_by_type,
    get_total_program_seats,
    get_inquiries_by_status,
    get_open_vs_resolved_inquiries
)

def print_separator(char="-", length=85):
    print(char * length)

# --- Display Tables ---

def display_services(services):
    if not services:
        print("No services found.")
        return
    print_separator()
    print(f"{'ID':<10} | {'Service Name':<30} | {'Category':<20} | {'Price ($)':<10} | {'Status':<10}")
    print_separator()
    for s in services:
        print(f"{s.service_id:<10} | {s.name[:28]:<30} | {s.category[:18]:<20} | {s.price:<10.2f} | {s.status:<10}")
    print_separator()
    print(f"Total: {len(services)} record(s)\n")

def display_programs(programs):
    if not programs:
        print("No programs found.")
        return
    print_separator("-", 92)
    print(f"{'ID':<10} | {'Program Title':<34} | {'Type':<14} | {'Duration':<10} | {'Seats':<6} | {'Status':<10}")
    print_separator("-", 92)
    for p in programs:
        print(f"{p.program_id:<10} | {p.title[:32]:<34} | {p.program_type[:12]:<14} | {p.duration[:9]:<10} | {p.seats:<6} | {p.status:<10}")
    print_separator("-", 92)
    print(f"Total: {len(programs)} record(s)\n")

def display_customers(customers):
    if not customers:
        print("No customers found.")
        return
    print_separator()
    print(f"{'ID':<10} | {'Customer Name':<20} | {'Company':<22} | {'Email':<25} | {'Phone':<12}")
    print_separator()
    for c in customers:
        print(f"{c.customer_id:<10} | {c.name[:18]:<20} | {c.company[:20]:<22} | {c.email[:23]:<25} | {c.phone:<12}")
    print_separator()
    print(f"Total: {len(customers)} record(s)\n")

def display_inquiries(inquiries):
    if not inquiries:
        print("No inquiries found.")
        return
    print_separator("=", 105)
    print(f"{'ID':<10} | {'Customer':<18} | {'Linked':<18} | {'Subject':<30} | {'Date':<10} | {'Status':<12}")
    print_separator("-", 105)
    for i in inquiries:
        link_str = f"{i.entity_type} {i.entity_id}"
        print(f"{i.inquiry_id:<10} | {i.customer_name[:16]:<18} | {link_str:<18} | {i.subject[:28]:<30} | {i.date:<10} | {i.status:<12}")
    print_separator("=", 105)
    print(f"Total: {len(inquiries)} record(s)\n")

# --- Service Sub-menu ---

def handle_service_menu(service_mgr):
    while True:
        print("\n" + "=" * 45)
        print("        SERVICE MANAGEMENT MENU")
        print("=" * 45)
        print("1. View All Services")
        print("2. Add New Service")
        print("3. Search Services")
        print("4. Filter Services by Status")
        print("5. Update Service Status")
        print("6. Delete a Service")
        print("7. Back to Main Menu")
        print("=" * 45)

        choice = input("Enter choice (1-7): ").strip()
        if choice == "1":
            print("\n--- All Technology Services ---")
            display_services(service_mgr.get_all_services())
        elif choice == "2":
            print("\n--- Add New Technology Service ---")
            sid = input("Enter Service ID (e.g. SRV-112): ").strip()
            name = input("Enter Service Name: ").strip()
            cat = input("Enter Category: ").strip()
            price = input("Enter Price ($): ").strip()
            dur = input("Enter Duration (e.g. 4 weeks): ").strip()
            st = input("Enter Status (Active/Inactive) [Default: Active]: ").strip()
            if not st:
                st = "Active"
            try:
                new_s = service_mgr.add_service(sid, name, cat, price, dur, st)
                print(f"\nSuccess: Service '{new_s.service_id} - {new_s.name}' added.")
            except ValueError as e:
                print(f"\nValidation Error: {e}")
            except Exception as e:
                print(f"\nError: {e}")
        elif choice == "3":
            kw = input("\nEnter search keyword (name or category): ").strip()
            try:
                results = service_mgr.search_services(kw)
                print(f"\nFound {len(results)} service(s) for '{kw}':")
                display_services(results)
            except ValueError as e:
                print(f"\nInput Error: {e}")
        elif choice == "4":
            st = input("\nEnter status to filter (Active/Inactive): ").strip()
            try:
                results = service_mgr.filter_by_status(st)
                print(f"\nFound {len(results)} service(s) with status '{st}':")
                display_services(results)
            except ValueError as e:
                print(f"\nValidation Error: {e}")
        elif choice == "5":
            sid = input("\nEnter Service ID to update: ").strip()
            new_st = input("Enter New Status (Active/Inactive): ").strip()
            try:
                updated = service_mgr.update_status(sid, new_st)
                print(f"\nSuccess: Service '{updated.service_id}' status updated to '{updated.status}'.")
            except KeyError as e:
                print(f"\nNot Found Error: {e.args[0]}")
            except ValueError as e:
                print(f"\nValidation Error: {e}")
        elif choice == "6":
            sid = input("\nEnter Service ID to delete: ").strip()
            confirm = input(f"Are you sure you want to delete '{sid}'? (y/n): ").strip().lower()
            if confirm == "y":
                try:
                    deleted = service_mgr.delete_service(sid)
                    print(f"\nSuccess: Service '{deleted.service_id} - {deleted.name}' deleted.")
                except KeyError as e:
                    print(f"\nNot Found Error: {e.args[0]}")
            else:
                print("Deletion cancelled.")
        elif choice == "7":
            break
        else:
            print("Invalid option. Please choose 1-7.")

# --- Program Sub-menu ---

def handle_program_menu(program_mgr):
    while True:
        print("\n" + "=" * 45)
        print("        PROGRAM MANAGEMENT MENU")
        print("=" * 45)
        print("1. View All Programs")
        print("2. Add New Program")
        print("3. Filter Programs by Type")
        print("4. Filter Programs by Status")
        print("5. Update Program Status")
        print("6. Delete a Program")
        print("7. Back to Main Menu")
        print("=" * 45)

        choice = input("Enter choice (1-7): ").strip()
        if choice == "1":
            print("\n--- All Technology & Training Programs ---")
            display_programs(program_mgr.get_all_programs())
        elif choice == "2":
            print("\n--- Add New Program ---")
            pid = input("Enter Program ID (e.g. PRG-211): ").strip()
            title = input("Enter Program Title: ").strip()
            ptype = input("Enter Type (Technology/Training/Internship): ").strip()
            duration = input("Enter Duration (e.g. 8 weeks): ").strip()
            seats = input("Enter Available Seats (e.g. 25): ").strip()
            status = input("Enter Status (Open/Ongoing/Closed) [Default: Open]: ").strip()
            if not status:
                status = "Open"
            try:
                new_p = program_mgr.add_program(pid, title, ptype, duration, seats, status)
                print(f"\nSuccess: Program '{new_p.program_id} - {new_p.title}' added.")
            except ValueError as e:
                print(f"\nValidation Error: {e}")
            except Exception as e:
                print(f"\nError: {e}")
        elif choice == "3":
            ptype = input("\nEnter Type to filter (Technology/Training/Internship): ").strip()
            try:
                results = program_mgr.filter_by_type(ptype)
                print(f"\nFound {len(results)} program(s) of type '{ptype}':")
                display_programs(results)
            except ValueError as e:
                print(f"\nValidation Error: {e}")
        elif choice == "4":
            st = input("\nEnter Status to filter (Open/Ongoing/Closed): ").strip()
            try:
                results = program_mgr.filter_by_status(st)
                print(f"\nFound {len(results)} program(s) with status '{st}':")
                display_programs(results)
            except ValueError as e:
                print(f"\nValidation Error: {e}")
        elif choice == "5":
            pid = input("\nEnter Program ID to update: ").strip()
            new_st = input("Enter New Status (Open/Ongoing/Closed): ").strip()
            try:
                updated = program_mgr.update_status(pid, new_st)
                print(f"\nSuccess: Program '{updated.program_id}' status updated to '{updated.status}'.")
            except KeyError as e:
                print(f"\nNot Found Error: {e.args[0]}")
            except ValueError as e:
                print(f"\nValidation Error: {e}")
        elif choice == "6":
            pid = input("\nEnter Program ID to delete: ").strip()
            confirm = input(f"Are you sure you want to delete '{pid}'? (y/n): ").strip().lower()
            if confirm == "y":
                try:
                    deleted = program_mgr.delete_program(pid)
                    print(f"\nSuccess: Program '{deleted.program_id} - {deleted.title}' deleted.")
                except KeyError as e:
                    print(f"\nNot Found Error: {e.args[0]}")
            else:
                print("Deletion cancelled.")
        elif choice == "7":
            break
        else:
            print("Invalid option. Please choose 1-7.")

# --- Inquiry Sub-menu ---

def handle_inquiry_menu(inquiry_mgr, service_mgr, program_mgr):
    while True:
        print("\n" + "=" * 45)
        print("   CUSTOMER & INQUIRY MANAGEMENT MENU")
        print("=" * 45)
        print("1. View All Inquiries")
        print("2. Log New Inquiry")
        print("3. Update Inquiry Status")
        print("4. View All Customers")
        print("5. Add New Customer")
        print("6. Back to Main Menu")
        print("=" * 45)

        choice = input("Enter choice (1-6): ").strip()
        if choice == "1":
            print("\n--- All Customer Inquiries ---")
            display_inquiries(inquiry_mgr.get_all_inquiries())
        elif choice == "2":
            print("\n--- Log New Customer Inquiry ---")
            inq_id = input("Enter Inquiry ID (e.g. INQ-511): ").strip()
            cust_id = input("Enter Existing Customer ID (e.g. CUST-401): ").strip()
            
            # Check customer existence
            customer = inquiry_mgr.find_customer_by_id(cust_id)
            if not customer:
                print(f"\nNotice: Customer '{cust_id}' not found.")
                create_now = input("Would you like to register this new customer now? (y/n): ").strip().lower()
                if create_now == "y":
                    cname = input("Enter Customer Name: ").strip()
                    cemail = input("Enter Email: ").strip()
                    cphone = input("Enter Phone: ").strip()
                    ccomp = input("Enter Company [Default: Individual]: ").strip()
                    try:
                        customer = inquiry_mgr.add_customer(cust_id, cname, cemail, cphone, ccomp)
                        print(f"Customer '{customer.name}' registered successfully.")
                    except ValueError as e:
                        print(f"\nValidation Error: {e}")
                        continue
                else:
                    print("Inquiry logging cancelled.")
                    continue

            link_type = input("Link to Service or Program? (Service/Program): ").strip()
            link_id = input("Enter Linked Service/Program ID (e.g. SRV-101 or PRG-201): ").strip()
            subject = input("Enter Subject: ").strip()
            message = input("Enter Inquiry Message: ").strip()
            date = input("Enter Date (YYYY-MM-DD) [Press Enter for today]: ").strip()
            status = input("Enter Status (New/In Progress/Resolved/Closed) [Default: New]: ").strip()
            if not status:
                status = "New"

            valid_s_ids = [s.service_id for s in service_mgr.get_all_services()]
            valid_p_ids = [p.program_id for p in program_mgr.get_all_programs()]

            try:
                new_inq = inquiry_mgr.log_inquiry(
                    inquiry_id=inq_id,
                    customer_id=customer.customer_id,
                    entity_type=link_type,
                    entity_id=link_id,
                    subject=subject,
                    message=message,
                    valid_service_ids=valid_s_ids,
                    valid_program_ids=valid_p_ids,
                    date=date,
                    status=status
                )
                print(f"\nSuccess: Inquiry '{new_inq.inquiry_id}' logged for customer '{new_inq.customer_name}'.")
            except (ValueError, KeyError) as e:
                print(f"\nError: {e.args[0] if isinstance(e, KeyError) else e}")
            except Exception as e:
                print(f"\nUnexpected Error: {e}")

        elif choice == "3":
            inq_id = input("\nEnter Inquiry ID to update: ").strip()
            new_st = input("Enter New Status (New/In Progress/Resolved/Closed): ").strip()
            try:
                updated = inquiry_mgr.update_inquiry_status(inq_id, new_st)
                print(f"\nSuccess: Inquiry '{updated.inquiry_id}' status updated to '{updated.status}'.")
            except KeyError as e:
                print(f"\nNot Found Error: {e.args[0]}")
            except ValueError as e:
                print(f"\nValidation Error: {e}")

        elif choice == "4":
            print("\n--- All Registered Customers ---")
            display_customers(inquiry_mgr.get_all_customers())

        elif choice == "5":
            print("\n--- Register New Customer ---")
            cid = input("Enter Customer ID (e.g. CUST-411): ").strip()
            name = input("Enter Full Name: ").strip()
            email = input("Enter Email: ").strip()
            phone = input("Enter Phone: ").strip()
            comp = input("Enter Company [Default: Individual]: ").strip()
            try:
                new_c = inquiry_mgr.add_customer(cid, name, email, phone, comp)
                print(f"\nSuccess: Customer '{new_c.customer_id} - {new_c.name}' registered.")
            except ValueError as e:
                print(f"\nValidation Error: {e}")
            except Exception as e:
                print(f"\nError: {e}")

        elif choice == "6":
            break
        else:
            print("Invalid option. Please choose 1-6.")

# --- Search & Filter Sub-menu ---

def handle_search_filter_menu(service_mgr, program_mgr, inquiry_mgr):
    while True:
        print("\n" + "=" * 45)
        print("        SEARCH & FILTER MENU")
        print("=" * 45)
        print("1. Universal Search (Across Everything)")
        print("2. Search & Filter Services")
        print("3. Search & Filter Programs")
        print("4. Search & Filter Inquiries")
        print("5. Back to Main Menu")
        print("=" * 45)

        choice = input("Enter choice (1-5): ").strip()
        if choice == "1":
            kw = input("\nEnter search keyword: ").strip()
            if not kw:
                print("Search term cannot be empty.")
                continue
            results = universal_search(
                service_mgr.get_all_services(),
                program_mgr.get_all_programs(),
                inquiry_mgr.get_all_inquiries(),
                kw
            )
            print(f"\n--- Universal Search Results for '{kw}' ---")
            print(f"\nMatching Services ({len(results['services'])}):")
            display_services(results['services'])
            print(f"Matching Programs ({len(results['programs'])}):")
            display_programs(results['programs'])
            print(f"Matching Inquiries ({len(results['inquiries'])}):")
            display_inquiries(results['inquiries'])

        elif choice == "2":
            kw = input("Enter service keyword (optional, press Enter to skip): ").strip()
            cat = input("Enter category (optional, press Enter to skip): ").strip()
            st = input("Enter status (optional, press Enter to skip): ").strip()
            
            services = service_mgr.get_all_services()
            if kw:
                services = search_services(services, kw)
            filtered = filter_services(services, category=cat, status=st)
            print(f"\nShowing {len(filtered)} matching service(s):")
            display_services(filtered)

        elif choice == "3":
            kw = input("Enter program keyword (optional, press Enter to skip): ").strip()
            ptype = input("Enter program type (optional, press Enter to skip): ").strip()
            st = input("Enter status (optional, press Enter to skip): ").strip()
            
            programs = program_mgr.get_all_programs()
            if kw:
                programs = search_programs(programs, kw)
            filtered = filter_programs(programs, program_type=ptype, status=st)
            print(f"\nShowing {len(filtered)} matching program(s):")
            display_programs(filtered)

        elif choice == "4":
            kw = input("Enter inquiry keyword (optional, press Enter to skip): ").strip()
            st = input("Enter status (New/In Progress/Resolved/Closed, optional): ").strip()
            etype = input("Enter linked type (Service/Program, optional): ").strip()

            inquiries = inquiry_mgr.get_all_inquiries()
            if kw:
                inquiries = search_inquiries(inquiries, kw)
            filtered = filter_inquiries(inquiries, status=st, entity_type=etype)
            print(f"\nShowing {len(filtered)} matching inquiry/inquiries:")
            display_inquiries(filtered)

        elif choice == "5":
            break
        else:
            print("Invalid option. Please choose 1-5.")

# --- Business Reports Sub-menu ---

def handle_reports_menu(service_mgr, program_mgr, inquiry_mgr):
    while True:
        print("\n" + "=" * 45)
        print("        BUSINESS REPORTS MENU")
        print("=" * 45)
        print("1. Full Business & Operations Summary Report")
        print("2. Services Breakdown by Category")
        print("3. Programs Breakdown by Type & Total Seats")
        print("4. Inquiries Status & Resolution Metrics")
        print("5. Back to Main Menu")
        print("=" * 45)

        choice = input("Enter choice (1-5): ").strip()
        services = service_mgr.get_all_services()
        programs = program_mgr.get_all_programs()
        inquiries = inquiry_mgr.get_all_inquiries()

        if choice == "1":
            print_business_report(services, programs, inquiries)
        elif choice == "2":
            cats = get_services_by_category(services)
            print("\n--- Services Breakdown by Category ---")
            print(f"{'Category':<30} | {'Count':<10}")
            print("-" * 45)
            for c, count in sorted(cats.items()):
                print(f"{c:<30} | {count:<10}")
            print(f"Total Services: {len(services)}\n")
        elif choice == "3":
            types = get_programs_by_type(programs)
            seats = get_total_program_seats(programs)
            print("\n--- Programs by Type & Capacity ---")
            for t, count in sorted(types.items()):
                print(f"{t:<20}: {count} program(s)")
            print(f"Total Available Seats Across Programs: {seats['total_seats']}")
            print(f"  - Seats in Open Programs:    {seats['seats_by_status'].get('Open', 0)}")
            print(f"  - Seats in Ongoing Programs: {seats['seats_by_status'].get('Ongoing', 0)}")
            print(f"  - Seats in Closed Programs:  {seats['seats_by_status'].get('Closed', 0)}\n")
        elif choice == "4":
            stats = get_inquiries_by_status(inquiries)
            res = get_open_vs_resolved_inquiries(inquiries)
            print("\n--- Inquiries Status & Resolution ---")
            for st, count in stats.items():
                print(f"{st:<20}: {count}")
            print(f"Total Inquiries:  {res['total']}")
            print(f"Active / Open:    {res['open_count']} ({res['open_pct']:.1f}%)")
            print(f"Resolved / Closed: {res['resolved_count']} ({res['resolved_pct']:.1f}%)\n")
        elif choice == "5":
            break
        else:
            print("Invalid option. Please choose 1-5.")

# --- Main Menu Loop ---

def show_main_menu():
    print("=" * 55)
    print("  VEDA TECHNOLOGY - BUSINESS & SERVICE MANAGEMENT")
    print("  Day 2: Programs, Inquiries, Search & Reports")
    print("=" * 55)
    print("1. Service Management")
    print("2. Program Management")
    print("3. Customer & Inquiry Management")
    print("4. Search & Filter Records")
    print("5. Business Reports")
    print("6. Exit")
    print("=" * 55)

def main():
    service_mgr = ServiceManager()
    program_mgr = ProgramManager()
    inquiry_mgr = InquiryManager()

    while True:
        try:
            show_main_menu()
            choice = input("Enter choice (1-6): ").strip()

            if choice == "1":
                handle_service_menu(service_mgr)
            elif choice == "2":
                handle_program_menu(program_mgr)
            elif choice == "3":
                handle_inquiry_menu(inquiry_mgr, service_mgr, program_mgr)
            elif choice == "4":
                handle_search_filter_menu(service_mgr, program_mgr, inquiry_mgr)
            elif choice == "5":
                handle_reports_menu(service_mgr, program_mgr, inquiry_mgr)
            elif choice == "6":
                print("\nThank you for using Veda Technology Service Management System. Goodbye!")
                break
            else:
                print("\nInvalid choice. Please select an option from 1 to 6.\n")
        except (KeyboardInterrupt, EOFError):
            print("\nExiting application. Goodbye!")
            break

if __name__ == "__main__":
    main()
