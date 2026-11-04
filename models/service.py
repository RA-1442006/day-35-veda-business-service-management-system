# Model representing a digital or tech service offered by Veda Technology

class Service:
    def __init__(self, service_id, name, category, price, duration, status="Active"):
        self.service_id = service_id
        self.name = name
        self.category = category
        self.price = float(price)
        self.duration = duration
        self.status = status

    def to_dict(self):
        # Convert object to dictionary for JSON storage
        return {
            "service_id": self.service_id,
            "name": self.name,
            "category": self.category,
            "price": self.price,
            "duration": self.duration,
            "status": self.status
        }

    @classmethod
    def from_dict(cls, data):
        # Create Service object from dictionary
        return cls(
            service_id=data.get("service_id", ""),
            name=data.get("name", ""),
            category=data.get("category", ""),
            price=data.get("price", 0.0),
            duration=data.get("duration", ""),
            status=data.get("status", "Active")
        )

    def __str__(self):
        return f"[{self.service_id}] {self.name} | Category: {self.category} | Price: ${self.price:.2f} | Duration: {self.duration} | Status: {self.status}"
