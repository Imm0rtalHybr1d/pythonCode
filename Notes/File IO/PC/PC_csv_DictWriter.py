import csv

cpu:str = input('Give PC CPU: ')
ram:str = input('Give PC RAM: ')
storage:str= input('Give PC Storage: ')
motherboard:str= input('Give PC Mothboard: ')

with open(fr"File IO/PC/pc.csv", mode='a') as file:
    dict_writer = csv.DictWriter(file,fieldnames=['CPU','RAM','Storage','Motherboard'])
    
    dict_writer.writerow({'CPU':cpu, 'RAM':ram,'Storage':storage,'Motherboard':motherboard})
    