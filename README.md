# Veda Technology Business & Service Management System

A Python console application that manages the daily operations of a technology and digital services company like Veda Technology. It handles technology offerings, client inquiries, training and internship programs, and service requests.

> Note: All records and client details used in this project are 100% synthetic (fake) and intended solely for learning and demonstration purposes. No real, private, or production data is used.

---

## Day 1 Progress & Roadmap

### What is Completed Today (Day 1)
- Project directory setup and modular architecture.
- Base data models for `Service`, `Program`, `Customer`, and `Inquiry`.
- Complete **Service Management Module** supporting:
  - Viewing all services
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

### Roadmap for Upcoming Days
- **Day 2**: Technology & Training Program Management (internship programs, certifications, student enrollment).
- **Day 3**: Customer Management & Inquiries Tracking (client profiles, service requests, ticketing workflow).
- **Day 4**: Business Analytics & Reporting (revenue breakdown, active client reports, export features, polishing).

---

## Folder Structure

```text
day-35-veda-business-service-management-system/
├── main.py                     # Main console menu application
├── models/                     # Core business entities
│   ├── service.py              # Service class model
│   ├── program.py              # Training/Internship program model
│   ├── customer.py             # Client/Customer model
│   └── inquiry.py              # Customer inquiry model
├── modules/                    # Application logic & helpers
│   ├── service_manager.py      # Service CRUD operations
│   ├── storage.py              # JSON file reading & writing
│   └── validators.py           # Input validation rules
├── data/
│   └── services.json           # Initial synthetic services dataset
├── output/
│   └── sample_output.txt       # Real execution transcript
├── README.md                   # Project overview & documentation
├── .gitignore                  # Git ignore rules
└── requirements.txt            # Project dependencies
```

---

## How to Run

### Requirements
- Python 3.8+ (tested on Python 3.14)
- No external libraries needed for Day 1 (uses Python standard library)

### Steps
1. Open the project folder in VS Code or your terminal:
   ```bash
   cd day-35-veda-business-service-management-system
   ```

2. Run the main program:
   ```bash
   python main.py
   ```

3. Follow the numbered menu options on screen to view, add, search, filter, update, or delete services.

---

## Features Completed in Day 1

1. **Service Model & Data Persistence**:
   - Each service has an ID, name, category, price, duration, and status.
   - Automatically reads from and writes to `data/services.json`.

2. **Validation**:
   - Prevents empty inputs.
   - Enforces unique Service IDs (no duplicates).
   - Validates that price is a positive numerical value.
   - Enforces allowed statuses (`Active`, `Inactive`).

3. **Exception Handling**:
   - Gracefully handles missing files or invalid JSON syntax.
   - Handles missing service IDs during update or delete operations without crashing.
   - Clean application exit.
