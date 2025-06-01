import json
import csv
from typing import Any, Dict, List

# Function to convert JSON to CSV
def json_to_csv(json_data: List[Dict[str, Any]], csv_file: str) -> None:
    # Get the keys from the first dictionary as the header
    if not json_data:
        print("No data provided to convert.")
        return
    header = json_data[0].keys()
    
    # Write to CSV file
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()  # Write the header
        writer.writerows(json_data)  # Write the data rows
    print(f"Data successfully written to {csv_file}")

# Example JSON data
json_example = [
    {"name": "Alice", "age": 30, "city": "New York"},
    {"name": "Bob", "age": 25, "city": "Los Angeles"}
]

# Convert JSON to CSV (output will be printed to console)
json_to_csv(json_example, 'output.csv')