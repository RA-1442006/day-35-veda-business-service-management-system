# Validation helper functions for user inputs

def is_not_empty(value, field_name="Field"):
    if not value or not str(value).strip():
        raise ValueError(f"{field_name} cannot be empty.")
    return str(value).strip()

def validate_service_id(service_id, existing_ids):
    cleaned_id = is_not_empty(service_id, "Service ID").upper()
    
    # Check for duplicate IDs
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
    # Validate each field one by one
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
