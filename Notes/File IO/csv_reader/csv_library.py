import csv

students = []
with open(fr"File IO\csv_reader\students_home.csv") as file:
    reader = csv.DictReader(file)    
    for row in reader:
        students.append({'name': row['name'], 'home': row['home']})
        
    
# sorted_list = 

for student in sorted(students, key=lambda student: student['name']):
    print(f"{student['name']} lives at {student['home']} ")