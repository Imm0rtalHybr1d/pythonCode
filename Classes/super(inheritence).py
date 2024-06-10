from typing import override

class Shape:
    def __init__(self, name:str,sides:int) -> None:
        self.name = name
        self.sides = sides
        
    def describe(self)->None:
        print(f'{self.name} ({self.sides} sides)')
        
    def shape_method(self) -> None:
        print(f'{self.name}: shape_method()')    
        
class Square(Shape):
    def __init__(self, size:float ) :
        super().__init__('Square',4)#super keyword needs to be used when inheriting from another class
    #we use super() to refer to the base class, then .__init__ to class its initializer method  
    # and pass in the relavant variables to that classes initiallzer
        self.size = size
        
    @override  #use the overide keyword to overide the describe method that is in the parent class already   
    #Indicate that a method is intended to override a method in a base class
    def describe(self) -> None:
         print(f'I am a {self.name} with a size of {self.size}')   

class Rectangle(Shape):
    def __init__(self, length:float,height:float) -> None:
        super().__init__('Rectangle', 4)   
        self.length = length
        self.height = height

    @override  #use the overide keyword to overide the describe method that is in the parent class already   
    #Indicate that a method is intended to override a method in a base class
    def describe(self) -> None:
        print(f'{self.name} ({self.length} x {self.height})')

def main():
    #creating an istance of our square class
    square:Square = Square(3)
    square.describe()
    square.shape_method()
    
    #creating an instance of the Rectangle class
    rectangle:Rectangle = Rectangle(5.5,2.6)
    rectangle.describe()
    rectangle.shape_method()
    
             
if __name__  == '__main__':
    main()
    

        