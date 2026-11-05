import os
from models.program import Program
from modules.storage import load_json, save_json
from modules.validators import validate_program_inputs, validate_program_status, validate_program_type

class ProgramManager:
    def __init__(self, file_path=None):
        if file_path is None:
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            self.file_path = os.path.join(base_dir, "data", "programs.json")
        else:
            self.file_path = file_path

        self.programs = []
        self.load_programs()

    def load_programs(self):
        raw_data = load_json(self.file_path)
        self.programs = [Program.from_dict(item) for item in raw_data]

    def save_programs(self):
        data = [prg.to_dict() for prg in self.programs]
        return save_json(self.file_path, data)

    def get_existing_ids(self):
        return [prg.program_id for prg in self.programs]

    def add_program(self, program_id, title, program_type, duration, seats, status="Open", fees=0.0):
        existing_ids = self.get_existing_ids()
        validated = validate_program_inputs(
            program_id=program_id,
            title=title,
            program_type=program_type,
            duration=duration,
            seats=seats,
            status=status,
            existing_ids=existing_ids
        )

        new_prg = Program(
            program_id=validated["program_id"],
            title=validated["title"],
            program_type=validated["type"],
            duration=validated["duration"],
            seats=validated["seats"],
            status=validated["status"],
            fees=fees
        )

        self.programs.append(new_prg)
        self.save_programs()
        return new_prg

    def get_all_programs(self):
        return self.programs

    def find_by_id(self, program_id):
        cleaned_id = str(program_id).strip().upper()
        for prg in self.programs:
            if prg.program_id.upper() == cleaned_id:
                return prg
        return None

    def filter_by_type(self, program_type):
        valid_type = validate_program_type(program_type)
        return [p for p in self.programs if p.program_type.lower() == valid_type.lower()]

    def filter_by_status(self, status):
        valid_status = validate_program_status(status)
        return [p for p in self.programs if p.status.lower() == valid_status.lower()]

    def update_status(self, program_id, new_status):
        program = self.find_by_id(program_id)
        if not program:
            raise KeyError(f"Program with ID '{program_id}' does not exist.")

        valid_status = validate_program_status(new_status)
        program.status = valid_status
        self.save_programs()
        return program

    def delete_program(self, program_id):
        program = self.find_by_id(program_id)
        if not program:
            raise KeyError(f"Program with ID '{program_id}' does not exist.")

        self.programs.remove(program)
        self.save_programs()
        return program
