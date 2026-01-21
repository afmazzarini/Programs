import csv

data = [
    {'Name': 'Magnus Carlsen', 'Rating': 2870},
    {'Name': 'Fabiano Caruana', 'Rating': 2822},
    {'Name': 'Ding Liren', 'Rating': 2801}
]

fieldnames = ['Name', 'Rating']
file_path = 'players.csv'

with open(file_path, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()  # Write the header row
    writer.writerows(data) # Write all data rows

print(f"CSV file '{file_path}' created successfully.")