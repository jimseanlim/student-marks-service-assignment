import json
import random
from datetime import datetime, timedelta

# Define the number of entries and the output filename
num_entries = 60
output_filename = "student_marks.json"

data = []

# Generate random data
for _ in range(num_entries):
    # Generate a random timestamp within a specific date range (e.g., one year)
    start_date = datetime(2023, 1, 1)
    end_date = start_date + timedelta(days=365)
    timestamp = start_date + random.random() * (end_date - start_date)

    # Generate random student ID and marks
    student_id = random.randint(1, 60)
    mark = random.randint(50, 100)

    data.append({
        "timestamp": timestamp.isoformat(),
        "student_id": student_id,
        "mark": mark
    })

# Create the JSON object
json_data = {"data": data}

# Write the JSON data to a file
with open(output_filename, "w") as json_file:
    json.dump(json_data, json_file, indent=2)

print(f"JSON data saved to {output_filename}")
