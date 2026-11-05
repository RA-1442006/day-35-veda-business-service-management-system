# Model representing technology, training, and internship programs

class Program:
    def __init__(self, program_id, title, program_type, duration, seats, status="Open", fees=0.0):
        self.program_id = program_id
        self.title = title
        self.program_type = program_type  # Technology, Training, or Internship
        self.duration = duration
        self.seats = int(seats)
        self.status = status  # Open, Ongoing, Closed
        self.fees = float(fees)

    def to_dict(self):
        return {
            "program_id": self.program_id,
            "title": self.title,
            "type": self.program_type,
            "duration": self.duration,
            "seats": self.seats,
            "status": self.status,
            "fees": self.fees
        }

    @classmethod
    def from_dict(cls, data):
        # Support both 'type' and 'program_type' keys for compatibility
        ptype = data.get("type") or data.get("program_type", "Training")
        return cls(
            program_id=data.get("program_id") or data.get("id", ""),
            title=data.get("title", ""),
            program_type=ptype,
            duration=data.get("duration", ""),
            seats=data.get("seats", 20),
            status=data.get("status", "Open"),
            fees=data.get("fees", 0.0)
        )

    def __str__(self):
        return f"[{self.program_id}] {self.title} | Type: {self.program_type} | Duration: {self.duration} | Seats: {self.seats} | Status: {self.status}"
