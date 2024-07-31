import csv #imports csv library
import car_class

cars_list:list[str]= []  #creates a empty list, which is meant to hold a dictionary representing a car and its attributes

#opens the file cars.csv 
with open(fr'cars.csv') as file:
    fieldnames = ['brand', 'model', 'colour', 'top_speed', 'v_type'] #specifies fieldnames that we need to pass as kword args for the DictReader
    reader = csv.DictReader(file, fieldnames=fieldnames) #creates the reader/iterator
    #reader iterates over each row using csv.DictReader  
    next(reader)  #skips header line 
    
    for car in reader:
       cars_list.append(car)       
       
       my_car: car_class.Car = car_class.Car(car['brand'],car['model'],car['colour'],car['top_speed'],car['v_type'])       
       my_car.display_car()

# for car in cars_list:
#         print(car['brand'],car['model'],car['colour'],car['top_speed'],car['v_type'])       