# Model representing customer inquiries linked to services or programs

class Inquiry:
    def __init__(self, inquiry_id, customer_id, customer_name, entity_type, entity_id, subject, message, date, status="New"):
        self.inquiry_id = inquiry_id
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.entity_type = entity_type  # Service or Program
        self.entity_id = entity_id      # e.g. SRV-101 or PRG-201
        self.subject = subject
        self.message = message
        self.date = date
        self.status = status            # New, In Progress, Resolved, Closed

    def to_dict(self):
        return {
            "inquiry_id": self.inquiry_id,
            "customer_id": self.customer_id,
            "customer_name": self.customer_name,
            "entity_type": self.entity_type,
            "entity_id": self.entity_id,
            "subject": self.subject,
            "message": self.message,
            "date": self.date,
            "status": self.status
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            inquiry_id=data.get("inquiry_id") or data.get("id", ""),
            customer_id=data.get("customer_id", ""),
            customer_name=data.get("customer_name", ""),
            entity_type=data.get("entity_type", "Service"),
            entity_id=data.get("entity_id", ""),
            subject=data.get("subject", ""),
            message=data.get("message", ""),
            date=data.get("date", ""),
            status=data.get("status", "New")
        )

    def __str__(self):
        return f"[{self.inquiry_id}] {self.customer_name} ({self.customer_id}) | Linked: {self.entity_type} {self.entity_id} | Subject: {self.subject} | Status: {self.status}"
