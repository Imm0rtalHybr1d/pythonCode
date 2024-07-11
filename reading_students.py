
# This Python code snippet is reading data from a CSV file named "students.csv" and creating a list of
# dictionaries where each dictionary represents a student with their name and house. It then sorts the
# list of students alphabetically by their names and finally prints out each student's name and house
# in the sorted order.
students = []
with open("students.csv") as file:
  for line in file:
    
    name, house = line.rstrip().split(",") 
    student = {'name':name, 'house':house}
    students.append(student)

sorted_list:sorted = sorted(students, key=lambda student: student['name'] )

for student in sorted_list:
  print(f"{student['name']} is in {student['house']}")