# Veda Technology Business & Service Management System

A modular Python console application representing the operations of a technology and digital-services organization like Veda Technology. It provides end-to-end management of technology services, training and internship programs, customer accounts, service inquiries, and business reporting.

> **Important Note:** All data (services, programs, client details, and inquiries) used in this application is 100% public or synthetic (fake). It is created strictly for academic and skill development purposes. Never connects to any private or production systems.

---

## Objective

The objective of this project is to apply foundational and intermediate Python programming concepts—functions, modular architecture, object-oriented programming (OOP), dictionaries, lists, file handling with JSON, input validation, defensive exception handling, and reporting—to build a realistic business management software.

---

## Tools & Environment

- **Language:** Python 3.8+ (tested on Python 3.14)
- **Editor / IDE:** VS Code
- **Data Persistence:** JSON (file handling via `json` and `os`)
- **Version Control:** Git & GitHub
- **Dependencies:** Python Standard Library only (`os`, `sys`, `json`, `datetime`) — zero external third-party packages required.

---

## Features

1. **Service Management (`modules/service_manager.py`)**:
   - Complete record lifecycle: add new services, view in formatted tables, search by name or category, filter by status (`Active` / `Inactive`), update status, and safe delete.
   - **Referential Integrity**: Safe-deletion guard checks `inquiries.json` before deleting a service. If linked inquiries exist, deletion is safely blocked with a clear warning to prevent dangling references.

2. **Program Management (`modules/program_manager.py`)**:
   - Manage three distinct program categories: `Technology`, `Training`, and `Internship`.
   - Track program status (`Open`, `Ongoing`, `Closed`), durations, fees, and seat capacity.
   - Safe deletion check preventing deletion of programs linked to active inquiries.

3. **Customer & Inquiry Tracking (`modules/inquiry_manager.py`)**:
   - Customer profile registry with phone and email validation.
   - Log service and program inquiries linked directly to validated service or program IDs.
   - Track inquiry lifecycle status: `New` -> `In Progress` -> `Resolved` -> `Closed`.

4. **Search and Filtering (`modules/search_filter.py`)**:
   - **Universal Keyword Search**: Query across services, programs, and inquiries simultaneously.
   - Multi-criteria filtering by category, type, and status with full case-insensitivity.
   - Explicit user notifications whenever a search or filter yields zero results.

5. **Executive Business Reports & File Export (`modules/reports.py`)**:
   - Services breakdown by business category.
   - Program breakdown by type and seat capacity (open vs ongoing vs closed).
   - Inquiry status metrics and resolution efficiency percentage.
   - Executive enterprise overview with overall totals.
   - Direct export functionality to save reports to `output/business_summary_report.txt`.

6. **Robust Validation & Exception Handling (`modules/validators.py` & `modules/storage.py`)**:
   - Strict validation for non-empty fields, positive numbers (prices and seats), allowed types/statuses, email/phone formats, and unique IDs.
   - Fault-tolerant JSON handling: gracefully recovers if data files are missing or corrupt without crashing the application.

---

## Folder Structure

```text
day-35-veda-business-service-management-system/
├── main.py                          # Application entry point with department sub-menus
├── models/                          # Core domain entity classes
│   ├── service.py                   # Service model with dictionary serialization
│   ├── program.py                   # Program model (Technology, Training, Internship)
│   ├── customer.py                  # Client / Customer model
│   └── inquiry.py                   # Customer inquiry model (linked entity)
├── modules/                         # Business logic and helper modules
│   ├── service_manager.py           # Service CRUD & data persistence
│   ├── program_manager.py           # Program CRUD & seat tracking
│   ├── inquiry_manager.py           # Customer registry & inquiry lifecycle
│   ├── search_filter.py             # Universal search & targeted multi-filters
│   ├── reports.py                   # Business analytics, totals & report export
│   ├── storage.py                   # Safe, fault-tolerant JSON read/write operations
│   └── validators.py                # Reusable input validation rules
├── data/                            # Synthetic JSON databases (100% fake)
│   ├── services.json                # Tech & digital services records
│   ├── programs.json                # Technology, training & internship programs
│   ├── customers.json               # Client & enterprise customer accounts
│   └── inquiries.json               # Inquiries referencing services & programs
├── output/                          # Execution transcripts & report exports
│   ├── sample_output.txt            # Day 1 test run transcript
│   ├── day2_sample_output.txt       # Day 2 test run transcript
│   ├── day3_sample_output.txt       # Day 3 test run transcript
│   ├── final_sample_output.txt      # Day 4 complete end-to-end execution transcript
│   └── business_summary_report.txt  # Saved executive business report export
├── README.md                        # Comprehensive project documentation
├── .gitignore                       # Git ignore rules (__pycache__, .vscode, *.pyc)
└── requirements.txt                 # Project environment dependencies (standard library)
```

---

## How to Run

### Requirements
- Python 3.8 or higher installed on your machine.
- No external libraries needed (runs entirely on Python's built-in standard library).

### Running the App
1. Open terminal and navigate into the project directory:
   ```bash
   cd day-35-veda-business-service-management-system
   ```

2. Run the main script:
   ```bash
   python main.py
   ```

3. Navigate the clean, numbered interactive menus:
   - `1`: Service Management
   - `2`: Program Management
   - `3`: Customer & Inquiry Management
   - `4`: Search & Filter Records
   - `5`: Business Reports
   - `6`: Exit

---

## Development Approach (Day 1 to Day 4)

Here is how I designed and implemented this project day-by-day:

### Day 1 (Internship Day 35): Foundation & Service Management
- **Concepts Used:** Functions, Modules, Classes, Lists, Dictionaries, Basic File I/O, Basic Exception Handling.
- Set up the modular directory layout (`models/`, `modules/`, `data/`, `output/`).
- Built the `Service` model and initial skeleton models for `Program`, `Customer`, and `Inquiry`.
- Implemented `modules/storage.py` for reading and writing JSON lists of dictionaries.
- Implemented `modules/service_manager.py` with full CRUD operations.
- Built input validation for duplicate IDs, empty values, and positive pricing in `validators.py`.
- Created interactive CLI menu loop in `main.py` and saved initial run logs in `output/sample_output.txt`.

### Day 2 (Internship Day 36): Programs, Customers & Inquiries
- **Concepts Used:** Relational Entity Linking, Date Handling, Sub-menu Navigation, Advanced Validation.
- Completed `Program`, `Customer`, and `Inquiry` models.
- Built `program_manager.py` with seat capacity tracking and program types (`Technology`, `Training`, `Internship`).
- Built `inquiry_manager.py` allowing customer registration and inquiry logging strictly linked to existing services or programs.
- Added universal keyword search across multiple lists and multi-attribute filters in `search_filter.py`.
- Designed initial business reports in `reports.py` and organized `main.py` into departmental sub-menus.

### Day 3 (Internship Day 37): Data Integrity, Resilient Storage & Export
- **Concepts Used:** Data Integrity Guards, String Formatting, File Writing, Fault Tolerance.
- Added relational safety guards: prevents deleting services or programs that have active linked inquiries.
- Enhanced search to be completely case-insensitive across all fields, providing clear zero-match notifications.
- Created executive business summary report calculating overall totals and resolution efficiency.
- Added direct report file export functionality to `output/business_summary_report.txt`.
- Enhanced `storage.py` to gracefully detect corrupt JSON data and recover safely without crashing.

### Day 4 (Internship Day 38): Final Polish, Testing & Deliverables
- **Concepts Used:** Defensive Programming, Edge-Case Verification, Code Quality, Comprehensive Testing.
- Conducted full regression testing across every menu and sub-menu path (wrong types, empty strings, negative inputs, missing IDs, linked-delete warnings, and corrupt file simulations).
- Removed redundant code, cleaned comments, standardized console messages, and ensured `.gitignore` excludes all cache files.
- Executed the complete end-to-end interactive session and recorded the transcript in `output/final_sample_output.txt`.
- Finalized comprehensive project documentation in `README.md`.

---

## Sample Output Files

Real, unedited execution logs are saved in the `output/` directory:
- [`output/sample_output.txt`](output/sample_output.txt): Day 1 service management test run.
- [`output/day2_sample_output.txt`](output/day2_sample_output.txt): Day 2 program, customer, and inquiry test run.
- [`output/day3_sample_output.txt`](output/day3_sample_output.txt): Day 3 data integrity and corrupt-file recovery test run.
- [`output/final_sample_output.txt`](output/final_sample_output.txt): Complete Day 4 end-to-end execution transcript covering all features and edge cases.
- [`output/business_summary_report.txt`](output/business_summary_report.txt): Real exported executive business report text file.

---

## Outcome and Learnings

Through this 4-day capstone project, I learned:
1. **Software Architecture**: How to structure a multi-tier Python application separating data models, storage logic, business managers, validation, and presentation.
2. **Data Consistency**: How to enforce relational integrity in file-based storage systems by checking foreign references before allowing deletions.
3. **Defensive Coding**: Designing functions that validate user input strictly (types, empty strings, bounds) and handle runtime exceptions gracefully so the app never terminates unexpectedly.
4. **Clean Code & Git Workflow**: Writing readable, beginner-friendly code with natural commits documenting incremental feature additions.

---

## Possible Future Improvements

1. **Relational Database Backend**: Migrate storage from JSON files to SQLite or PostgreSQL using SQL or an ORM like SQLAlchemy.
2. **CSV / Excel Bulk Import & Export**: Add utilities to import bulk customer and service catalogs from CSV files.
3. **Web Interface**: Build a lightweight FastAPI or Flask REST API with a modern web dashboard.
4. **Authentication & Roles**: Implement user authentication with role-based access control (Admin, Manager, Staff).
