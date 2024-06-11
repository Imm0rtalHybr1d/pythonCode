from typing import Self
from datetime import date

class Calculator:
    def __init__(self, version:int) -> None:
        self.version = version
        
    def description(self) ->None: #instance method 
        print(f'Currently running version: {self.version}')

    #@staticmethod doesnt rely on the class, and can be used anywhere
    #general reason for using it within, is that it compliments the class well
    @staticmethod #makes no changes to the class or instance itself/ 
    def add_numbers( *numbers:float) -> float:
        return sum(numbers)
    
def main():
    cal1: Calculator = Calculator(1)
    cal2: Calculator = Calculator(2)
    
    #calls instance methods
    cal1.description()
    cal2.description()
    
    #calls static method , can be called without instantiating the class
    print(Calculator.add_numbers(1,2,3,4,5))
    
    
    
 
if __name__ == "__main__":
    main()
     