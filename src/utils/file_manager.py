import os
import json
import csv
from typing import List, Dict, Any

def get_all_files(directory: str, extension: str = ".pdf") -> List[str]:
    """
    Returns a list of all files in the given directory with the specified extension.
    """
    files = []
    for filename in os.listdir(directory):
        if filename.lower().endswith(extension.lower()):
            files.append(os.path.join(directory, filename))
    return files

def save_json(data: Any, filepath: str) -> None:
    """
    Saves data to a JSON file.
    """
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def save_csv(data: List[Dict[str, Any]], filepath: str, fieldnames: List[str]) -> None:
    """
    Saves a list of dictionaries to a CSV file.
    """
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def load_json(filepath: str) -> Any:
    """
    Loads data from a JSON file.
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)
