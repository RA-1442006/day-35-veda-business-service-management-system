# Veda Technology Business & Service Management System

A Python console application that manages the daily operations of a technology and digital services company like Veda Technology. It handles technology offerings, client inquiries, training and internship programs, customer accounts, and operational reporting.

> Note: All records and client details used in this project are 100% synthetic (fake) and intended solely for learning and demonstration purposes. No real, private, or production data is used.

---

## Project Progress & Roadmap

### Day 1 Progress (Internship Day 35)
- Project directory setup and modular architecture.
- Base data models for `Service`, `Program`, `Customer`, and `Inquiry`.
- Complete **Service Management Module** supporting:
  - Viewing all services in a clean tabular view
  - Adding new services with validation
  - Searching services by name or category
  - Filtering services by status (`Active` / `Inactive`)
  - Updating service status
  - Deleting services safely
- JSON data persistence (`data/services.json`) via `storage.py`.
- Input validation in `validators.py` (empty inputs, data types, duplicate IDs).
- Exception handling for missing records, bad inputs, and corrupt/missing JSON files.
- Menu-driven console interface in `main.py`.
- Sample run logs recorded in `output/sample_output.txt`.

### Day 2 Progress (Internship Day 36)
- **Program Management (`modules/program_manager.py`)**:
  - Full CRUD operations: add, view all, filter by type/status, update status, delete.
  - Supports Program Types: `Technology`, `Training`, `Internship`.
  - Supports Program Statuses: `Open`, `Ongoing`, `Closed`.
  - Fields tracked: `program_id`, `title`, `type`, `duration`, `seats`, `status`, `fees`.
  - Synthetic dataset seeded in `data/programs.json` (10 records).
- **Customer & Inquiry Management (`modules/inquiry_manager.py`)**:
  - Full `Customer` and `Inquiry` models in `models/customer.py` and `models/inquiry.py`.
  - Customer directory and registration with validation (email and phone checks).
  - Logging customer inquiries strictly linked to valid existing services or programs.
  - Inquiry status lifecycle: `New`, `In Progress`, `Resolved`, `Closed`.
  - Synthetic datasets seeded in `data/customers.json` and `data/inquiries.json` (10 records each).
- **Search & Filtering Module (`modules/search_filter.py`)**:
  - Universal keyword search across services, programs, and inquiries in a single query.
  - Multi-attribute targeted filters (category, type, status, linked entity).
- **Basic Business Reports (`modules/reports.py`)**:
  - Services breakdown by category.
  - Programs breakdown by type and total available seats capacity.
  - Inquiry status distribution and resolution metrics (active vs resolved %).
  - Full summary business dashboard printed directly to console.
- **Console Interface Enhancement (`main.py`)**:
  - Redesigned main menu with clean, organized sub-menus for each department.
  - Robust error handling for invalid input and missing records without app crashes.
- Real execution transcript recorded in `output/day2_sample_output.txt`.

### Day 3 Progress (Internship Day 37)
- **Data Integrity & Relational Safety Guards**:
  - Added relational reference checks in `inquiry_manager.py` and `main.py` (`get_inquiries_for_entity`, `get_inquiries_for_customer`).
  - Implemented safe deletion logic: actively warns the user and blocks deletion of any Service or Program currently linked to active customer inquiries, preventing broken or orphan references.
- **Enhanced Search & Filtering (`modules/search_filter.py`)**:
  - Fully case-insensitive keyword searching across all entity attributes.
  - Added explicit, friendly "no matching records found" user feedback when queries or filter criteria yield zero matches.
- **Executive Business Reports & File Export (`modules/reports.py`)**:
  - Created comprehensive executive summary report with overall enterprise totals (total services, programs, clients, inquiries, seats capacity, and resolution percentage).
  - Added text export feature (`save_report_to_file`) saving complete timestamped business reports directly to `output/business_summary_report.txt`.
- **Fault-Tolerant JSON Storage & Corrupt File Recovery (`modules/storage.py`)**:
  - Enhanced JSON error handling with user-friendly warnings when encountering malformed or corrupted data files.
  - Tested zero-crash recovery: automatically falls back to clean in-memory state while notifying the user.
- **Unified Menu & Sub-Menu Polishing (`main.py`)**:
  - Standardized all sub-menu prompts, table formatting, and success/error message patterns.
- Real execution transcript recorded in `output/day3_sample_output.txt`.

### Roadmap for Upcoming Days
- **Day 4 (Internship Day 38)**: Final project integration, multi-format export utilities (CSV/JSON), edge-case regression test suite, code documentation review, and final packaging for deployment.

---

## Folder Structure

```text
day-35-veda-business-service-management-system/
├── main.py                     # Main console application with department sub-menus
├── models/                     # Core business entities
│   ├── service.py              # Service model
│   ├── program.py              # Program model (Technology, Training, Internship)
│   ├── customer.py             # Customer/Client model
│   └── inquiry.py              # Inquiry model (linked to service or program)
├── modules/                    # Business logic & operational helpers
│   ├── service_manager.py      # Service CRUD operations
│   ├── program_manager.py      # Program CRUD operations & capacity tracking
│   ├── inquiry_manager.py      # Customer & Inquiry lifecycle management
│   ├── search_filter.py        # Universal search & targeted filtering
│   ├── reports.py              # Business analytics, summary totals & file export
│   ├── storage.py              # Fault-tolerant JSON file reading & writing
│   └── validators.py           # Input validation across all models
├── data/                       # Synthetic datasets (100% fake)
│   ├── services.json           # Tech & digital services records
│   ├── programs.json           # Tech, training & internship programs
│   ├── customers.json          # Client & business customer accounts
│   └── inquiries.json          # Customer inquiries linked to services/programs
├── output/                     # Execution transcripts & saved reports
│   ├── sample_output.txt       # Day 1 sample run transcript
│   └── day2_sample_output.txt  # Day 2 sample run transcript
│   ├── day3_sample_output.txt  # Day 3 sample run transcript
│   └── business_summary_report.txt # Saved executive business report
├── README.md                   # Project documentation & progress logs
├── .gitignore                  # Git ignore rules
└── requirements.txt            # Project dependencies (standard library)
```

---

## How to Run

### Requirements
- Python 3.8+ (tested on Python 3.14)
- No external libraries required (uses Python standard library: `os`, `sys`, `json`, `datetime`)

### Steps
1. Navigate to the project root directory:
   ```bash
   cd day-35-veda-business-service-management-system
   ```

2. Run the application:
   ```bash
   python main.py
   ```

3. Navigate through the top-level departments using the numbered menus:
   - `1`: Service Management (View, Add, Search, Filter, Update, Safe Delete)
   - `2`: Program Management (View, Add, Filter by Type/Status, Update, Safe Delete)
   - `3`: Customer & Inquiry Management (Inquiries, Customer Registration, Status Updates)
   - `4`: Search & Filter Records (Universal search and filtered queries with zero-result feedback)
   - `5`: Business Reports (Executive totals, category breakdown, seats capacity, and text file export)
   - `6`: Exit

---

## Features Completed So Far

1. **Service Management**:
   - Add, view, search, filter, update status, and safe delete tech services.
   - Relational link check blocks deletion if inquiries reference the service.
   - Persistent storage in `data/services.json`.

2. **Program Management**:
   - Manage Technology programs, Corporate Trainings, and Internships.
   - Track available seats and status (`Open`, `Ongoing`, `Closed`).
   - Relational link check blocks deletion if inquiries reference the program.
   - Persistent storage in `data/programs.json`.

3. **Customer & Inquiry Tracking**:
   - Maintain customer profiles with email and phone validation.
   - Log inquiries linked to actual services or programs.
   - Inquiry status lifecycle (`New` -> `In Progress` -> `Resolved` -> `Closed`).
   - Persistent storage in `data/customers.json` and `data/inquiries.json`.

4. **Universal Search & Filtering**:
   - Case-insensitive search across all three entity types with a single search term.
   - Multi-attribute targeted filters with explicit feedback when no records match.

5. **Operational Reports & Export**:
   - Services breakdown by business category.
   - Programs by type and total seat capacity.
   - Inquiries resolution efficiency metrics.
   - Overall enterprise summary totals.
   - Export full report to `output/business_summary_report.txt`.

6. **Defensive Validation & Exception Handling**:
   - Input validation for types, ranges, duplicate IDs, and entity link validity.
   - Zero-crash recovery when missing or corrupt JSON files are encountered.
