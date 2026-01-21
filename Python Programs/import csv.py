import csv

data = [
    ["Name", "Age", "City"],
    ["Aman", 28, "Pune"],
    ["Poonam", 24, "Jaipur"],
    ["Bobby", 32, "Delhi"]
]

file_path = 'people.csv'

# Open the file in write mode ('w') with newline=''
with open(file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write all rows at once
    writer.writerows(data)

print(f"CSV file '{file_path}' created successfully.")