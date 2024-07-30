# This Python code snippet is reading data from a CSV file named 'pc.csv' that contains information
# about computer parts such as CPU, RAM, and storage. Here is a breakdown of what the code is doing:
import csv

parts_list:list = []
parts_dict:dict = {}

with open(fr"File IO/PC/pc.csv") as file:
    reader = csv.DictReader(file)    
          
    for row in reader:        
        parts_list.append({'CPU':row['CPU'],
                           'RAM':row['RAM'],
                           'Storage':row['Storage'],
                           'Motherboard':row['Motherboard']})
        
for PC in parts_list:
    print(PC['CPU'], PC['RAM'], PC['Storage'], PC['Motherboard'])

    
