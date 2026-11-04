import json
import os

# Helper to load data from a json file safely
def load_json(file_path):
    # If the file doesn't exist yet, return an empty list
    if not os.path.exists(file_path):
        print(f"Notice: File {file_path} not found. Starting with empty records.")
        return []
    
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data
    except json.JSONDecodeError:
        print(f"Error: {file_path} contains invalid or corrupt JSON. Initializing empty list.")
        return []
    except Exception as e:
        print(f"Unexpected error while reading {file_path}: {e}")
        return []

# Helper to save data back into the json file
def save_json(file_path, data):
    try:
        # Make sure the target directory exists
        folder = os.path.dirname(file_path)
        if folder and not os.path.exists(folder):
            os.makedirs(folder, exist_ok=True)
            
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        return True
    except Exception as e:
        print(f"Error saving data to {file_path}: {e}")
        return False
