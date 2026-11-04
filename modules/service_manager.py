import os
from models.service import Service
from modules.storage import load_json, save_json
from modules.validators import validate_service_inputs, validate_status

class ServiceManager:
    def __init__(self, file_path=None):
        if file_path is None:
            # Default path relative to project root
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            self.file_path = os.path.join(base_dir, "data", "services.json")
        else:
            self.file_path = file_path
            
        self.services = []
        self.load_services()

    def load_services(self):
        # Load raw data from json and convert to Service objects
        raw_data = load_json(self.file_path)
        self.services = [Service.from_dict(item) for item in raw_data]

    def save_services(self):
        # Convert Service objects back to dictionaries and save
        data = [srv.to_dict() for srv in self.services]
        return save_json(self.file_path, data)

    def get_existing_ids(self):
        return [srv.service_id for srv in self.services]

    def add_service(self, service_id, name, category, price, duration, status="Active"):
        # Validate inputs first
        existing_ids = self.get_existing_ids()
        validated_data = validate_service_inputs(
            service_id=service_id,
            name=name,
            category=category,
            price=price,
            duration=duration,
            status=status,
            existing_ids=existing_ids
        )

        # Create new service instance
        new_service = Service(
            service_id=validated_data["service_id"],
            name=validated_data["name"],
            category=validated_data["category"],
            price=validated_data["price"],
            duration=validated_data["duration"],
            status=validated_data["status"]
        )

        self.services.append(new_service)
        self.save_services()
        return new_service

    def get_all_services(self):
        return self.services

    def find_by_id(self, service_id):
        cleaned_id = str(service_id).strip().upper()
        for srv in self.services:
            if srv.service_id.upper() == cleaned_id:
                return srv
        return None

    def search_services(self, keyword):
        # Search by service name or category (case-insensitive)
        if not keyword or not str(keyword).strip():
            raise ValueError("Search keyword cannot be empty.")
        
        term = str(keyword).strip().lower()
        results = []
        for srv in self.services:
            if term in srv.name.lower() or term in srv.category.lower():
                results.append(srv)
        return results

    def filter_by_status(self, status):
        # Filter by Active or Inactive
        valid_status = validate_status(status)
        results = [srv for srv in self.services if srv.status.lower() == valid_status.lower()]
        return results

    def update_status(self, service_id, new_status):
        # Check if service exists
        service = self.find_by_id(service_id)
        if not service:
            raise KeyError(f"Service with ID '{service_id}' does not exist.")

        # Validate the new status
        valid_status = validate_status(new_status)
        service.status = valid_status
        self.save_services()
        return service

    def delete_service(self, service_id):
        # Check if service exists
        service = self.find_by_id(service_id)
        if not service:
            raise KeyError(f"Service with ID '{service_id}' does not exist.")

        self.services.remove(service)
        self.save_services()
        return service
