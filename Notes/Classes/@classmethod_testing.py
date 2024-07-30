from typing import Self

class People:
    
    Defeciencies = ''
    def __init__(self,gender:str, name:str,surname:str,age:int ) -> None:
        self.gender = gender
        self.name = name
        self.surname = surname
        self.age = age
    
    def display_person(self): #instance method , this affects the instance of the class
        print(f'{self.name} {self.surname}')        
        print(self.gender)        
        print(self.age)    
        
    @classmethod #this method changes the default deciency for the entire class
    def add_defeciency(cls,defeciencies:str) -> None:
        cls.Defeciencies = defeciencies
    
    @staticmethod  #part of the class as it might relate to the class but doesnt affect the class
    def calculate_bmi(weight_kg: float, height_m: float) -> float:
        bmi = weight_kg / (height_m ** 2)
        return bmi 
    
        
            
        
def main():
    person:People = People('Male', 'Marciano','Martin',26)
    person.display_person()
    
    #access the class method to change the deficiency variable for the entire People class
    #this means all instances of the People class will have no defeciency 
    People.add_defeciency('No defeciency')
    print(f'All instance of the People class will have {People.defeciencies} as defeciency')
 
if __name__ == "__main__":
    main()
         