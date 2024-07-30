from typing import Self


# The class `Person` defines a simple data structure for storing a person's name and age, with methods
# for string representation and equality comparison.
class Person:
    def __init__(self,name:str,age:int) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f'{self.name}: {self.age}'

    def __eq__(self, other: Self ) -> bool:
        print('Current:', self.__dict__)
        print('Other:', other.__dict__)
        return self.__dict__ == other.__dict__
     
def main():
    mario: Person = Person('Carlo',22)  
    hano: Person = Person('Hano',26)
    Bano: Person = Person('Hiemie',25)
    
    if hano == mario:
        print('Yes')
    else:
        print('They are not the same ')    
     # we can compare objects using the __eq_ dunder method
    #it will return true because the hano.name is equal to mario.name
    
    # print(mario)
    # print(repr(mario)) #prints the object itself
if __name__ == '__main__':
    main()        
    
    