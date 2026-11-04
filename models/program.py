# Model representing tech training and internship programs

class Program:
    def __init__(self, program_id, title, program_type, duration, fees, status="Open"):
        self.program_id = program_id
        self.title = title
        self.program_type = program_type  # Internship, Certification, or Training
        self.duration = duration
        self.fees = float(fees)
        self.status = status  # Open, Ongoing, Closed

    def to_dict(self):
        return {
            "program_id": self.program_id,
            "title": self.title,
            "program_type": self.program_type,
            "duration": self.duration,
            "fees": self.fees,
            "status": self.status
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            program_id=data.get("program_id", ""),
            title=data.get("title", ""),
            program_type=data.get("program_type", "Training"),
            duration=data.get("duration", ""),
            fees=data.get("fees", 0.0),
            status=data.get("status", "Open")
        )

    def __str__(self):
        return f"[{self.program_id}] {self.title} ({self.program_type}) | Duration: {self.duration} | Fees: ${self.fees:.2f} | Status: {self.status}"
