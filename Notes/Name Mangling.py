class Car:
    __YEAR: int = 2000
    
    def __init__(self,brand:str , fuel_type:str) -> None:
        self.__brand = brand
        self.__fuel_type = fuel_type
        
        self.__var:str = 'red'        
        
    def drive(self) -> None:
        print(f'Driving {self.__brand}')
     
    def __get_description(self) -> None:
        print(f'{self.__brand}: {self.__fuel_type}')
        
    def display_colour(self) -> None :
        print(f'{self.__brand} is {self.__var.capitalize()}')    

class Toyota(Car):
    def __init__(self,fuel_type: str) -> None:
        super().__init__('toyota', fuel_type)
        self.var = 100
            
def main():
    car : Car = Car('Toyota','Electric')
    car.drive()
    
    # Name Mangling/ need to invoke _ClassName__func/var
    #mainly for use within the class itself
    car._Car__get_description()
    
    toyota : Toyota = Toyota('Electric')
    toyota.display_colour()
    
    
if __name__ == "__main__":
    main()
             