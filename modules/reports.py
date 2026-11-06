import os
from datetime import datetime

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

def get_overall_totals(services, programs, customers, inquiries):
    res_data = get_open_vs_resolved_inquiries(inquiries)
    seats_data = get_total_program_seats(programs)

    return {
        "total_services": len(services),
        "total_programs": len(programs),
        "total_customers": len(customers),
        "total_inquiries": len(inquiries),
        "total_seats": seats_data["total_seats"],
        "open_seats": seats_data["seats_by_status"].get("Open", 0),
        "open_inquiries": res_data["open_count"],
        "resolved_inquiries": res_data["resolved_count"],
        "resolution_rate": res_data["resolved_pct"]
    }

def build_business_report_text(services, programs, customers, inquiries):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    totals = get_overall_totals(services, programs, customers, inquiries)
    srv_cats = get_services_by_category(services)
    prg_types = get_programs_by_type(programs)
    seats_data = get_total_program_seats(programs)
    inq_stats = get_inquiries_by_status(inquiries)
    res_data = get_open_vs_resolved_inquiries(inquiries)

    lines = []
    lines.append("=" * 72)
    lines.append("        VEDA TECHNOLOGY - EXECUTIVE BUSINESS SUMMARY REPORT")
    lines.append("=" * 72)
    lines.append(f"Report Generated: {timestamp}")
    lines.append("Data Source: Synthetic Operational Records")
    lines.append("-" * 72)

    # 1. Executive Summary & Overall Totals
    lines.append("\n[1] Executive Summary & Overall Totals:")
    lines.append("-" * 50)
    lines.append(f"Total Technology Services Offered:  {totals['total_services']}")
    lines.append(f"Total Training/Tech Programs:      {totals['total_programs']}")
    lines.append(f"Total Registered Business Clients: {totals['total_customers']}")
    lines.append(f"Total Customer Inquiries Logged:   {totals['total_inquiries']}")
    lines.append(f"Total Program Seats Capacity:      {totals['total_seats']} (Open: {totals['open_seats']})")
    lines.append(f"Inquiry Resolution Efficiency:     {totals['resolution_rate']:.1f}%")

    # 2. Services by Category
    lines.append("\n[2] Services Breakdown by Category:")
    lines.append("-" * 50)
    lines.append(f"{'Category':<32} | {'Total Services':<15}")
    lines.append("-" * 50)
    for cat, count in sorted(srv_cats.items()):
        lines.append(f"{cat:<32} | {count:<15}")
    lines.append(f"Total Services: {len(services)}")

    # 3. Programs by Type & Seats Capacity
    lines.append("\n[3] Programs Breakdown by Type & Seats Capacity:")
    lines.append("-" * 50)
    lines.append(f"{'Program Type':<32} | {'Programs Count':<15}")
    lines.append("-" * 50)
    for ptype, count in sorted(prg_types.items()):
        lines.append(f"{ptype:<32} | {count:<15}")
    lines.append("-" * 50)
    lines.append(f"Total Programs Offered: {len(programs)}")
    lines.append(f"Total Seats Capacity:   {seats_data['total_seats']}")
    lines.append(f"  - Seats in Open Programs:    {seats_data['seats_by_status'].get('Open', 0)}")
    lines.append(f"  - Seats in Ongoing Programs: {seats_data['seats_by_status'].get('Ongoing', 0)}")
    lines.append(f"  - Seats in Closed Programs:  {seats_data['seats_by_status'].get('Closed', 0)}")

    # 4. Inquiries Status & Resolution Analysis
    lines.append("\n[4] Inquiries Status & Resolution Analysis:")
    lines.append("-" * 50)
    lines.append(f"{'Status':<25} | {'Count':<10}")
    lines.append("-" * 50)
    for st, count in inq_stats.items():
        lines.append(f"{st:<25} | {count:<10}")
    lines.append("-" * 50)
    lines.append(f"Total Inquiries Logged:  {res_data['total']}")
    lines.append(f"Active / Open Inquiries: {res_data['open_count']} ({res_data['open_pct']:.1f}%)")
    lines.append(f"Resolved / Closed:       {res_data['resolved_count']} ({res_data['resolved_pct']:.1f}%)")
    lines.append("=" * 72)

    return "\n".join(lines)

def print_business_report(services, programs, customers, inquiries):
    report_text = build_business_report_text(services, programs, customers, inquiries)
    print(report_text)
    print()

def save_report_to_file(report_text, file_path=None):
    if file_path is None:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = os.path.join(base_dir, "output", "business_summary_report.txt")
    
    # Ensure output directory exists
    folder = os.path.dirname(file_path)
    if folder and not os.path.exists(folder):
        os.makedirs(folder, exist_ok=True)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(report_text)

    return file_path
