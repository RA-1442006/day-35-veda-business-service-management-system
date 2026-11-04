# Model representing a client or business customer

class Customer:
    def __init__(self, customer_id, name, email, phone, company="Individual"):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone
        self.company = company

    def to_dict(self):
        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "company": self.company
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            customer_id=data.get("customer_id", ""),
            name=data.get("name", ""),
            email=data.get("email", ""),
            phone=data.get("phone", ""),
            company=data.get("company", "Individual")
        )

    def __str__(self):
        return f"[{self.customer_id}] {self.name} | Company: {self.company} | Email: {self.email} | Phone: {self.phone}"
