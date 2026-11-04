# Model representing customer inquiries and service requests

class Inquiry:
    def __init__(self, inquiry_id, customer_name, email, subject, message, date, status="Pending"):
        self.inquiry_id = inquiry_id
        self.customer_name = customer_name
        self.email = email
        self.subject = subject
        self.message = message
        self.date = date
        self.status = status  # Pending, In Progress, Resolved

    def to_dict(self):
        return {
            "inquiry_id": self.inquiry_id,
            "customer_name": self.customer_name,
            "email": self.email,
            "subject": self.subject,
            "message": self.message,
            "date": self.date,
            "status": self.status
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            inquiry_id=data.get("inquiry_id", ""),
            customer_name=data.get("customer_name", ""),
            email=data.get("email", ""),
            subject=data.get("subject", ""),
            message=data.get("message", ""),
            date=data.get("date", ""),
            status=data.get("status", "Pending")
        )

    def __str__(self):
        return f"[{self.inquiry_id}] From: {self.customer_name} ({self.email}) | Subject: {self.subject} | Date: {self.date} | Status: {self.status}"
