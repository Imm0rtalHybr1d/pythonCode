import csv
from pc_class import computer #import computer class

with open(fr'pc_list.csv') as pc_list_file: #open file and use csvreader to iterate over the rows
    reader = csv.reader(pc_list_file)
    
    for PC in pc_list_file: 
        CPU, GPU, RAM, Storage, Motherboard = PC.rsplit(',') #split the row by commas and store each split in variables representitive 
        
        #instantiate the computer class and use the values that were split 
        my_pc:computer = computer(CPU, GPU, RAM, Storage, Motherboard )  
        my_pc.pc_description()
 