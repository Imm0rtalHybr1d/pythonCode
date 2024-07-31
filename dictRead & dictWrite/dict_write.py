import csv



filed_name:list[str] = ['brand','model','colour','top_speed','v_type']


    
with open(fr'cars.csv', mode='a') as file:
    writer = csv.DictWriter(file, fieldnames=['brand','model','colour','top_speed','v_type'])
    
    writer.writeheader()
    for count in range(2):
            #request data from user 
        brand:str = input('Vehicle Brand: ')
        model:str = input('Vehicle model: ')
        colour:str = input('Vehicle colour: ')
        top_speed:str = input('Vehicle top speed: ')
        v_type:str = input('Vehicle type: ')
        print('')
        
        writer.writerow({'brand':brand,'model':model,'colour':colour,'top_speed':top_speed,'v_type':v_type})

    
    