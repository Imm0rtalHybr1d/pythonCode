#create a class called Car
class Car:
    #defining the car class 
    def __init__(self,brand:str,model:str,colour:str,wheels:int) -> None:
        self.brand = brand
        self.model = model
        self.colour = colour
        self.wheels = wheels
        
        
    def turn_on(self) -> None :
        print(f'Turning on {self.brand}{self.model}')
        
    def turn_off(self) -> None :
        print(f'Turning off {self.brand}')
    
    def drive(self, km:float) -> None :
        print(f'Driving {self.brand} for {km}km')
    
    def describe(self) -> None :
        print(f'Youre driving a  {self.brand} {self.model} ')
        print(f'The colour is {self.colour} and it has {self.wheels} wheels')


def main():
        bmw: Car =  Car('BMW','M5 Competition','Blue','4')
        bmw.turn_on()
        bmw.drive(20)
        bmw.describe()
        bmw.turn_off()
        print("")
        print("")
        volvo: Car = Car('Volvo', 'V40', 'Copper',4)
        volvo.turn_off()
        volvo.drive(25)
        volvo.describe()
        volvo.turn_off()
        
if __name__ == '__main__':
    main()