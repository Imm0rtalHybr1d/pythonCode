from abc import ABC, abstractmethod
from operator import truediv

class Appliance(ABC):
    def __init__(self,brand:str,version_no:int) -> None:
        self.brand = brand
        self.version_no = version_no
        self.is_turned_on: bool = False
        
        # super().__init__()
        
    @abstractmethod
    def turn_on(self) -> None:
        ...    
    @abstractmethod
    def turn_off(self) -> None:
        ...    
        
        
class Lamp(Appliance):
    def __init__(self,brand:str,version_no:int) -> None:     
        super().__init__(brand,version_no)
        
    def turn_on(self) -> None:
        if self.is_turned_on:
            print(f'{self.brand} is already turned on')  
        else:
            self.is_turned_on = True
            print(f'{self.brand} is now turned on')
            
            
    def turn_off(self) -> None:
        if self.is_turned_on:
            self.is_turned_on = False
            print(f'{self.brand} is turned off')  
        else:
             print(f'{self.brand} is already turned off')

class Oven(Appliance):
    def __init__(self, brand: str, version_no: int) -> None:
        super().__init__(brand, version_no)
             
def main():
    lamp:Lamp = Lamp('Swan', 2)
    lamp.turn_on()
    lamp.turn_on()
    lamp.turn_off()
    lamp.turn_off()
    lamp.turn_on()
    lamp.turn_off()
   
    oven: Oven = Oven('Defy', 10) 
    
 
if __name__ == "__main__":
    main()
              