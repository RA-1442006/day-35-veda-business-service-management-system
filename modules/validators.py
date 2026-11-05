# Validation helper functions for user inputs across services, programs, and inquiries

def is_not_empty(value, field_name="Field"):
    if value is None or not str(value).strip():
        raise ValueError(f"{field_name} cannot be empty.")
    return str(value).strip()

def validate_service_id(service_id, existing_ids):
    cleaned_id = is_not_empty(service_id, "Service ID").upper()
    for existing in existing_ids:
        if cleaned_id == existing.upper():
            raise ValueError(f"Service ID '{cleaned_id}' already exists. Please use a unique ID.")
    return cleaned_id

def validate_price(price_value):
    is_not_empty(price_value, "Price")
    try:
        price = float(price_value)
    except ValueError:
        raise ValueError("Price must be a valid number (e.g. 1500 or 1500.50).")
    
    if price <= 0:
        raise ValueError("Price must be greater than zero.")
    return price

def validate_status(status_value):
    is_not_empty(status_value, "Status")
    cleaned_status = status_value.strip().capitalize()
    allowed = ["Active", "Inactive"]
    if cleaned_status not in allowed:
        raise ValueError(f"Invalid status '{status_value}'. Allowed values are: Active, Inactive.")
    return cleaned_status

def validate_service_inputs(service_id, name, category, price, duration, status, existing_ids):
    valid_id = validate_service_id(service_id, existing_ids)
    valid_name = is_not_empty(name, "Service name")
    valid_category = is_not_empty(category, "Category")
    valid_price = validate_price(price)
    valid_duration = is_not_empty(duration, "Duration")
    valid_status = validate_status(status)

    return {
        "service_id": valid_id,
        "name": valid_name,
        "category": valid_category,
        "price": valid_price,
        "duration": valid_duration,
        "status": valid_status
    }

# --- Day 2 Program Validators ---

def validate_program_id(program_id, existing_ids):
    cleaned_id = is_not_empty(program_id, "Program ID").upper()
    for existing in existing_ids:
        if cleaned_id == existing.upper():
            raise ValueError(f"Program ID '{cleaned_id}' already exists. Please use a unique ID.")
    return cleaned_id

def validate_program_type(program_type):
    is_not_empty(program_type, "Program Type")
    cleaned_type = program_type.strip().title()
    allowed = ["Technology", "Training", "Internship"]
    if cleaned_type not in allowed:
        raise ValueError(f"Invalid program type '{program_type}'. Allowed types are: Technology, Training, Internship.")
    return cleaned_type

def validate_seats(seats_value):
    is_not_empty(seats_value, "Seats")
    try:
        seats = int(seats_value)
    except ValueError:
        raise ValueError("Seats must be a whole number (e.g. 25).")
    if seats <= 0:
        raise ValueError("Seats must be greater than zero.")
    return seats

def validate_program_status(status_value):
    is_not_empty(status_value, "Program Status")
    cleaned_status = status_value.strip().title()
    allowed = ["Open", "Ongoing", "Closed"]
    if cleaned_status not in allowed:
        raise ValueError(f"Invalid program status '{status_value}'. Allowed values are: Open, Ongoing, Closed.")
    return cleaned_status

def validate_program_inputs(program_id, title, program_type, duration, seats, status, existing_ids):
    valid_id = validate_program_id(program_id, existing_ids)
    valid_title = is_not_empty(title, "Program Title")
    valid_type = validate_program_type(program_type)
    valid_duration = is_not_empty(duration, "Duration")
    valid_seats = validate_seats(seats)
    valid_status = validate_program_status(status)

    return {
        "program_id": valid_id,
        "title": valid_title,
        "type": valid_type,
        "duration": valid_duration,
        "seats": valid_seats,
        "status": valid_status
    }

# --- Day 2 Customer & Inquiry Validators ---

def validate_customer_id(customer_id, existing_ids):
    cleaned_id = is_not_empty(customer_id, "Customer ID").upper()
    for existing in existing_ids:
        if cleaned_id == existing.upper():
            raise ValueError(f"Customer ID '{cleaned_id}' already exists. Please use a unique ID.")
    return cleaned_id

def validate_email(email_value):
    email = is_not_empty(email_value, "Email").lower()
    if "@" not in email or "." not in email:
        raise ValueError(f"Invalid email '{email_value}'. Please enter a valid email address.")
    return email

def validate_phone(phone_value):
    phone = is_not_empty(phone_value, "Phone number")
    # Check that phone has digits and reasonable length
    digits = [c for c in phone if c.isdigit()]
    if len(digits) < 7:
        raise ValueError("Phone number must contain at least 7 digits.")
    return phone

def validate_inquiry_id(inquiry_id, existing_ids):
    cleaned_id = is_not_empty(inquiry_id, "Inquiry ID").upper()
    for existing in existing_ids:
        if cleaned_id == existing.upper():
            raise ValueError(f"Inquiry ID '{cleaned_id}' already exists. Please use a unique ID.")
    return cleaned_id

def validate_inquiry_status(status_value):
    is_not_empty(status_value, "Inquiry Status")
    # Accept formats like "In Progress", "in progress", "resolved", etc.
    cleaned = status_value.strip()
    status_map = {
        "new": "New",
        "in progress": "In Progress",
        "inprogress": "In Progress",
        "resolved": "Resolved",
        "closed": "Closed"
    }
    key = cleaned.lower()
    if key not in status_map:
        raise ValueError(f"Invalid inquiry status '{status_value}'. Allowed values: New, In Progress, Resolved, Closed.")
    return status_map[key]

def validate_entity_link(entity_type, entity_id, valid_service_ids, valid_program_ids):
    is_not_empty(entity_type, "Link Type")
    is_not_empty(entity_id, "Linked ID")
    
    cleaned_type = entity_type.strip().title()
    cleaned_id = entity_id.strip().upper()

    if cleaned_type == "Service":
        valid_upper = [s.upper() for s in valid_service_ids]
        if cleaned_id not in valid_upper:
            raise KeyError(f"Service ID '{cleaned_id}' does not exist in services database.")
    elif cleaned_type == "Program":
        valid_upper = [p.upper() for p in valid_program_ids]
        if cleaned_id not in valid_upper:
            raise KeyError(f"Program ID '{cleaned_id}' does not exist in programs database.")
    else:
        raise ValueError(f"Invalid link type '{entity_type}'. Must be either 'Service' or 'Program'.")

    return cleaned_type, cleaned_id
