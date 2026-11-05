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

### Roadmap for Upcoming Days
- **Day 3 (Internship Day 37)**: Client relationship history, inquiry priority queues, automated follow-up workflows, and batch service updates.
- **Day 4 (Internship Day 38)**: Comprehensive business analytics, financial summary reports, CSV/JSON data exporting, and final project packaging.

---

## Folder Structure

```text
day-35-veda-business-service-management-system/
├── main.py                     # Main console application with sub-menus
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
│   ├── reports.py              # Business analytics & capacity metrics
│   ├── storage.py              # JSON file reading & writing utilities
│   └── validators.py           # Input validation across all models
├── data/                       # Synthetic datasets (100% fake)
│   ├── services.json           # Tech & digital services records
│   ├── programs.json           # Tech, training & internship programs
│   ├── customers.json          # Client & business customer accounts
│   └── inquiries.json          # Customer inquiries linked to services/programs
├── output/                     # Execution transcripts
│   ├── sample_output.txt       # Day 1 sample run transcript
│   └── day2_sample_output.txt  # Day 2 sample run transcript
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
   - `1`: Service Management
   - `2`: Program Management
   - `3`: Customer & Inquiry Management
   - `4`: Search & Filter Records
   - `5`: Business Reports
   - `6`: Exit

---

## Features Completed So Far

1. **Service Management**:
   - Add, view, search, filter, update status, and delete tech services.
   - Persistent storage in `data/services.json`.

2. **Program Management**:
   - Manage Technology programs, Corporate Trainings, and Internships.
   - Track available seats and status (`Open`, `Ongoing`, `Closed`).
   - Persistent storage in `data/programs.json`.

3. **Customer & Inquiry Tracking**:
   - Maintain customer profiles with email and phone validation.
   - Log inquiries linked to actual services or programs.
   - Update inquiry lifecycle (`New` -> `In Progress` -> `Resolved` -> `Closed`).
   - Persistent storage in `data/customers.json` and `data/inquiries.json`.

4. **Universal Search & Filtering**:
   - Search across all three entity types with a single search term.
   - Custom filters by category, program type, and status.

5. **Operational Reports**:
   - Services breakdown by business category.
   - Programs by type and total seat capacity.
   - Inquiries resolution rates (open vs resolved).

6. **Defensive Validation & Exception Handling**:
   - Guarantees valid numeric inputs, non-empty fields, unique IDs, and valid entity links.
   - Graceful handling of missing records and corrupted/missing files without application crashes.
