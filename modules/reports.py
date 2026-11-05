# Business reporting module for Veda Technology

def get_services_by_category(services):
    categories = {}
    for s in services:
        cat = s.category
        categories[cat] = categories.get(cat, 0) + 1
    return categories

def get_programs_by_type(programs):
    types = {}
    for p in programs:
        ptype = p.program_type
        types[ptype] = types.get(ptype, 0) + 1
    return types

def get_inquiries_by_status(inquiries):
    statuses = {}
    for i in inquiries:
        st = i.status
        statuses[st] = statuses.get(st, 0) + 1
    return statuses

def get_open_vs_resolved_inquiries(inquiries):
    open_count = 0
    resolved_count = 0
    
    for i in inquiries:
        st = i.status.lower()
        if st in ["new", "in progress"]:
            open_count += 1
        elif st in ["resolved", "closed"]:
            resolved_count += 1

    total = len(inquiries)
    open_pct = (open_count / total * 100) if total > 0 else 0.0
    resolved_pct = (resolved_count / total * 100) if total > 0 else 0.0

    return {
        "total": total,
        "open_count": open_count,
        "open_pct": open_pct,
        "resolved_count": resolved_count,
        "resolved_pct": resolved_pct
    }

def get_total_program_seats(programs):
    total_seats = 0
    seats_by_status = {"Open": 0, "Ongoing": 0, "Closed": 0}

    for p in programs:
        total_seats += p.seats
        st = p.status.title()
        seats_by_status[st] = seats_by_status.get(st, 0) + p.seats

    return {
        "total_seats": total_seats,
        "seats_by_status": seats_by_status
    }

def print_business_report(services, programs, inquiries):
    print("=" * 70)
    print("        VEDA TECHNOLOGY - BUSINESS & OPERATIONAL REPORT")
    print("=" * 70)

    # 1. Services by Category
    srv_cats = get_services_by_category(services)
    print("\n[1] Services Breakdown by Category:")
    print("-" * 50)
    print(f"{'Category':<30} | {'Total Services':<15}")
    print("-" * 50)
    for cat, count in sorted(srv_cats.items()):
        print(f"{cat:<30} | {count:<15}")
    print(f"Total Active/Offered Services: {len(services)}")

    # 2. Programs by Type & Total Seats
    prg_types = get_programs_by_type(programs)
    seats_data = get_total_program_seats(programs)
    print("\n[2] Programs Breakdown by Type & Seats Capacity:")
    print("-" * 50)
    print(f"{'Program Type':<30} | {'Programs Count':<15}")
    print("-" * 50)
    for ptype, count in sorted(prg_types.items()):
        print(f"{ptype:<30} | {count:<15}")
    print("-" * 50)
    print(f"Total Programs Offered: {len(programs)}")
    print(f"Total Seats Capacity:   {seats_data['total_seats']}")
    print(f"  - Seats in Open Programs:    {seats_data['seats_by_status'].get('Open', 0)}")
    print(f"  - Seats in Ongoing Programs: {seats_data['seats_by_status'].get('Ongoing', 0)}")
    print(f"  - Seats in Closed Programs:  {seats_data['seats_by_status'].get('Closed', 0)}")

    # 3. Inquiries by Status & Resolution Metrics
    inq_stats = get_inquiries_by_status(inquiries)
    res_data = get_open_vs_resolved_inquiries(inquiries)
    print("\n[3] Inquiries Status & Resolution Analysis:")
    print("-" * 50)
    print(f"{'Status':<25} | {'Count':<10}")
    print("-" * 50)
    for st, count in inq_stats.items():
        print(f"{st:<25} | {count:<10}")
    print("-" * 50)
    print(f"Total Inquiries Logged:  {res_data['total']}")
    print(f"Active / Open Inquiries: {res_data['open_count']} ({res_data['open_pct']:.1f}%)")
    print(f"Resolved / Closed:       {res_data['resolved_count']} ({res_data['resolved_pct']:.1f}%)")
    print("=" * 70)
    print()
