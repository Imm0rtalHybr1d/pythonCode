# This Python code snippet is reading data from a CSV file named 'pc.csv' that contains information
# about computer parts such as CPU, RAM, and storage. Here is a breakdown of what the code is doing:
import csv

parts_list:list = []
parts_dict:dict = {}

with open('PC\pc.csv') as file:
    reader = csv.reader(file)
    
    for row in reader:
        print(f'{row}')
        print(f'len = {len(row)}')
        print(f'{''}')
        
        
        
        
        
        
    # for cpu, ram, storage, motherboard in reader:        
    #     parts_dict = {'CPU': {cpu}, 'RAM': {ram}, 'Storage':{storage}, 'Motherboard':{motherboard}}
    #     parts_list.append([parts_dict['CPU'],parts_dict['RAM'],parts_dict['Storage'], parts_dict['Motherboard']])
        

        
# sorted_by_storage:list = sorted(parts_list )
# for cpu,ram,storage,motherboard in sorted_by_storage:
#     print(*cpu,*ram,*storage, *motherboard)
