import json
import os
from src.models import WeatherRecord
FILE_PATH = "data/data.json"

def save_and_clean(record: WeatherRecord):
    data = []
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(FILE_PATH), exist_ok=True)

    # Load existing data
    if os.path.exists(FILE_PATH) and os.path.getsize(FILE_PATH) > 0:
        with open(FILE_PATH, 'r') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []

    # Add new record
    data.append(record.to_json_dict())

    # Remove duplicates (Keep the most recent search per city)
    # Using a dict comprehension preserves the latest entry
    unique_data = {item['city'].lower(): item for item in data}
    final_list = list(unique_data.values())

    with open(FILE_PATH, 'w') as f:
        json.dump(final_list, f, indent=4)