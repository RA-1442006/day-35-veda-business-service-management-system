import sys
from modules.service_manager import ServiceManager

def print_separator():
    print("-" * 80)

def display_services(services):
    if not services:
        print("No services found.")
        return

    print_separator()
    print(f"{'ID':<10} | {'Service Name':<30} | {'Category':<20} | {'Price ($)':<10} | {'Status':<10}")
    print_separator()
    for srv in services:
        print(f"{srv.service_id:<10} | {srv.name[:28]:<30} | {srv.category[:18]:<20} | {srv.price:<10.2f} | {srv.status:<10}")
    print_separator()
    print(f"Total: {len(services)} record(s)\n")

def handle_view_all(manager):
    print("\n--- All Technology Services ---")
    services = manager.get_all_services()
    display_services(services)

def handle_add_service(manager):
    print("\n--- Add New Technology Service ---")
    service_id = input("Enter Service ID (e.g. SRV-111): ").strip()
    name = input("Enter Service Name: ").strip()
    category = input("Enter Category: ").strip()
    price = input("Enter Price ($): ").strip()
    duration = input("Enter Duration (e.g. 4 weeks): ").strip()
    status = input("Enter Status (Active/Inactive) [Default: Active]: ").strip()
    
    if not status:
        status = "Active"

    try:
        new_srv = manager.add_service(service_id, name, category, price, duration, status)
        print(f"\nSuccess: Service '{new_srv.service_id} - {new_srv.name}' has been added.")
    except ValueError as e:
        print(f"\nValidation Error: {e}")
    except Exception as e:
        print(f"\nError: Could not add service: {e}")

def handle_search(manager):
    print("\n--- Search Services ---")
    keyword = input("Enter search term (name or category): ").strip()
    try:
        results = manager.search_services(keyword)
        print(f"\nFound {len(results)} matching service(s) for '{keyword}':")
        display_services(results)
    except ValueError as e:
        print(f"\nInput Error: {e}")

def handle_filter_by_status(manager):
    print("\n--- Filter Services by Status ---")
    status = input("Enter status to filter (Active/Inactive): ").strip()
    try:
        results = manager.filter_by_status(status)
        print(f"\nShowing {len(results)} service(s) with status '{status}':")
        display_services(results)
    except ValueError as e:
        print(f"\nValidation Error: {e}")

def handle_update_status(manager):
    print("\n--- Update Service Status ---")
    service_id = input("Enter Service ID to update: ").strip()
    new_status = input("Enter New Status (Active/Inactive): ").strip()

    try:
        updated = manager.update_status(service_id, new_status)
        print(f"\nSuccess: Service '{updated.service_id}' status updated to '{updated.status}'.")
    except KeyError as e:
        print(f"\nNot Found Error: {e.args[0]}")
    except ValueError as e:
        print(f"\nValidation Error: {e}")

def handle_delete_service(manager):
    print("\n--- Delete Service ---")
    service_id = input("Enter Service ID to delete: ").strip()
    confirm = input(f"Are you sure you want to delete service '{service_id}'? (y/n): ").strip().lower()
    
    if confirm != "y":
        print("Deletion cancelled.")
        return

    try:
        deleted = manager.delete_service(service_id)
        print(f"\nSuccess: Service '{deleted.service_id} - {deleted.name}' has been deleted.")
    except KeyError as e:
        print(f"\nNot Found Error: {e.args[0]}")

def show_menu():
    print("=" * 50)
    print(" Veda Technology - Business & Service Management")
    print(" Day 1: Foundation & Service Management")
    print("=" * 50)
    print("1. View All Services")
    print("2. Add New Service")
    print("3. Search Services (by Name or Category)")
    print("4. Filter Services by Status")
    print("5. Update Service Status")
    print("6. Delete a Service")
    print("7. Exit")
    print("=" * 50)

def main():
    manager = ServiceManager()

    while True:
        try:
            show_menu()
            choice = input("Enter your choice (1-7): ").strip()

            if choice == "1":
                handle_view_all(manager)
            elif choice == "2":
                handle_add_service(manager)
            elif choice == "3":
                handle_search(manager)
            elif choice == "4":
                handle_filter_by_status(manager)
            elif choice == "5":
                handle_update_status(manager)
            elif choice == "6":
                handle_delete_service(manager)
            elif choice == "7":
                print("\nThank you for using Veda Technology Service Management System. Goodbye!")
                break
            else:
                print("\nInvalid choice. Please select an option from 1 to 7.\n")
        except (KeyboardInterrupt, EOFError):
            print("\nExiting application. Goodbye!")
            break

if __name__ == "__main__":
    main()
