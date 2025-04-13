import json
import os

def load_data(file_path='data.json'):
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            return json.load(f)
    return {}

def save_data(data, file_path='data.json'):
    with open(file_path, 'w') as f:
        json.dump(data, f)