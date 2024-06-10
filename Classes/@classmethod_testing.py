from typing import Self

class People:
    
    Defeciencies = ''
    def __init__(self,gender:str, name:str,surname:str,age:int ) -> None:
        self.gender = gender
        self.name = name
        self.surname = surname
        self.age = age
        
        
    @classmethod #this method changes the default deciency for the entire class
    def add_defeciency(cls,defeciencies:str) -> None:
        cls.Defeciencies = defeciencies
    
    @staticmethod
    def test():
        return 
    
        
    def display_person(self):
        print(f'{self.name} {self.surname}')        
        print(self.gender)        
        print(self.age)        
        
def main():
    person:People = People('Male', 'Marciano','Martin',26)
    person.display_person()
    
    #access the class method to change the deficiency variable for the entire People class
    #this means all instances of the People class will have no defeciency 
    People.add_defeciency('No defeciency')
    print(People.defeciencies)
 
if __name__ == "__main__":
    main()
         