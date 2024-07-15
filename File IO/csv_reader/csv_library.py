import csv

students = []
with open("students_home.csv") as file:
    reader = csv.reader(file)
    next(reader)  # Optionally skip the header row if present
    for row in reader:
        name, *address = row  # Directly assign the first element as name and the rest as address
        students.append({'name': name, 'address': list(address)})
    
sorted_list = sorted(students, key=lambda student: student['name'])

for student in sorted_list:
    print(f"{student['name']} lives at {student['address']}")