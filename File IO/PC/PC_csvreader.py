# This Python code snippet is reading data from a CSV file named 'pc.csv' that contains information
# about computee r parts such as CPU, RAM, and storage. Heris a breakdown of what the code is doing:
import csv

parts_list:list = []
parts_dict:dict = {}

def read_lines(filepath:str) -> None:
    with open(filepath, mode='a') as file:
        reader = csv.reader(file)
        next(reader) #skips header row
            
        for cpu, ram, storage, motherboard in reader:        
            parts_dict = {'CPU': {cpu}, 'RAM': {ram}, 'Storage':{storage}, 'Motherboard':{motherboard}}
            parts_list.append((parts_dict['CPU'],parts_dict['RAM'],parts_dict['Storage'],parts_dict['Motherboard']))

def write_lines(filepath:str) -> None:
    user_specs:str = input('Enter the PC spects serparated by commas: ')
    cpu, ram, storage, motherboard = user_specs.rsplit(',')
    
    with open(filepath, mode='a') as file :
        writer = csv.writer(file)
        writer.writerow([cpu, ram, storage, motherboard])
        
def main():  
    filepath:str = fr"File IO/PC/pc.csv" 
    
    write_lines(filepath) # writes lines
    read_lines(filepath) # reads line from csv file into a list and then iterates over list and prints that item 
    
    for PC in parts_list:
        print(*PC)
    
 
if __name__ == "__main__":
    main()
     
