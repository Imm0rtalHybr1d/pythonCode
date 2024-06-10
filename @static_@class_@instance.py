from typing import Self
from datetime import date

class Calculator:
    def __init__(self, version:int) -> None:
        self.version = version
        
    def description(self) ->None: #instance method 
        print(f'Currently running version: {self.version}')

def main():
    cal1: Calculator = Calculator(1)
    cal2: Calculator = Calculator(2)
    
    cal1.description()
    cal2.description()
 
if __name__ == "__main__":
    main()
     