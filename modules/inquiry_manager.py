import os
from datetime import datetime
from models.customer import Customer
from models.inquiry import Inquiry
from modules.storage import load_json, save_json
from modules.validators import (
    is_not_empty,
    validate_customer_id,
    validate_email,
    validate_phone,
    validate_inquiry_id,
    validate_inquiry_status,
    validate_entity_link
)

class InquiryManager:
    def __init__(self, customers_path=None, inquiries_path=None):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
        self.customers_path = customers_path or os.path.join(base_dir, "data", "customers.json")
        self.inquiries_path = inquiries_path or os.path.join(base_dir, "data", "inquiries.json")

        self.customers = []
        self.inquiries = []
        
        self.load_customers()
        self.load_inquiries()

    # --- Customer Methods ---

    def load_customers(self):
        raw_data = load_json(self.customers_path)
        self.customers = [Customer.from_dict(item) for item in raw_data]

    def save_customers(self):
        data = [c.to_dict() for c in self.customers]
        return save_json(self.customers_path, data)

    def get_existing_customer_ids(self):
        return [c.customer_id for c in self.customers]

    def get_all_customers(self):
        return self.customers

    def find_customer_by_id(self, customer_id):
        cleaned_id = str(customer_id).strip().upper()
        for c in self.customers:
            if c.customer_id.upper() == cleaned_id:
                return c
        return None

    def add_customer(self, customer_id, name, email, phone, company="Individual"):
        existing_ids = self.get_existing_customer_ids()
        valid_id = validate_customer_id(customer_id, existing_ids)
        valid_name = is_not_empty(name, "Customer Name")
        valid_email = validate_email(email)
        valid_phone = validate_phone(phone)
        valid_company = is_not_empty(company, "Company") if company else "Individual"

        new_cust = Customer(
            customer_id=valid_id,
            name=valid_name,
            email=valid_email,
            phone=valid_phone,
            company=valid_company
        )

        self.customers.append(new_cust)
        self.save_customers()
        return new_cust

    # --- Inquiry Methods ---

    def load_inquiries(self):
        raw_data = load_json(self.inquiries_path)
        self.inquiries = [Inquiry.from_dict(item) for item in raw_data]

    def save_inquiries(self):
        data = [inq.to_dict() for inq in self.inquiries]
        return save_json(self.inquiries_path, data)

    def get_existing_inquiry_ids(self):
        return [inq.inquiry_id for inq in self.inquiries]

    def get_all_inquiries(self):
        return self.inquiries

    def find_inquiry_by_id(self, inquiry_id):
        cleaned_id = str(inquiry_id).strip().upper()
        for inq in self.inquiries:
            if inq.inquiry_id.upper() == cleaned_id:
                return inq
        return None

    def log_inquiry(self, inquiry_id, customer_id, entity_type, entity_id, subject, message, valid_service_ids, valid_program_ids, date=None, status="New"):
        # Validate customer existence
        customer = self.find_customer_by_id(customer_id)
        if not customer:
            raise KeyError(f"Customer ID '{customer_id}' does not exist. Please register the customer first.")

        # Validate unique inquiry ID
        existing_ids = self.get_existing_inquiry_ids()
        valid_inq_id = validate_inquiry_id(inquiry_id, existing_ids)

        # Validate link to existing service or program
        clean_type, clean_entity_id = validate_entity_link(entity_type, entity_id, valid_service_ids, valid_program_ids)

        valid_subject = is_not_empty(subject, "Subject")
        valid_message = is_not_empty(message, "Message")
        valid_status = validate_inquiry_status(status)

        if not date or not str(date).strip():
            date = datetime.now().strftime("%Y-%m-%d")

        new_inquiry = Inquiry(
            inquiry_id=valid_inq_id,
            customer_id=customer.customer_id,
            customer_name=customer.name,
            entity_type=clean_type,
            entity_id=clean_entity_id,
            subject=valid_subject,
            message=valid_message,
            date=str(date).strip(),
            status=valid_status
        )

        self.inquiries.append(new_inquiry)
        self.save_inquiries()
        return new_inquiry

    def update_inquiry_status(self, inquiry_id, new_status):
        inquiry = self.find_inquiry_by_id(inquiry_id)
        if not inquiry:
            raise KeyError(f"Inquiry with ID '{inquiry_id}' does not exist.")

        valid_status = validate_inquiry_status(new_status)
        inquiry.status = valid_status
        self.save_inquiries()
        return inquiry

    def filter_by_status(self, status):
        valid_status = validate_inquiry_status(status)
        return [inq for inq in self.inquiries if inq.status.lower() == valid_status.lower()]

    def delete_inquiry(self, inquiry_id):
        inquiry = self.find_inquiry_by_id(inquiry_id)
        if not inquiry:
            raise KeyError(f"Inquiry with ID '{inquiry_id}' does not exist.")

        self.inquiries.remove(inquiry)
        self.save_inquiries()
        return inquiry
