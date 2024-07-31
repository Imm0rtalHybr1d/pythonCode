import csv

for i in range(4):
        #get parts from user
    cpu:str = input('CPU: ')
    ram:str = input('RAM: ')
    gpu:str = input('GPU: ')
    storage:str= input('Storage: ')
    motherboard:str= input('Mothboard: ')
    
    with open(fr'pc_list.csv', mode='a') as pc_list_file:
        writer = csv.writer(pc_list_file)
        writer.writerow([cpu, gpu, ram, storage, motherboard])
    
    print(f'PC #{i+1} complete')
    print(f'{''}')
    
