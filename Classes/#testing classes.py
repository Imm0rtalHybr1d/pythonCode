class PC_spec:# creating a class called PC_spec
    #Initialize the class, define the class blueprint
    def __init__(self,CPU:str,GPU:str,RAM:str,motherboard:str,PSU:str,strorage:str) -> None:
        self.CPU = CPU
        self.GPU = GPU
        self.RAM = RAM
        self.motherboard = motherboard
        self.PSU = PSU
        self.strorage = strorage
    
    #creating simple functionality for the class    
    def specifications(self) -> None :
        print('Specifications: ')
        print(f'CPU: {self.CPU}')
        print(f'GPU: {self.GPU}')
        print(f'RAM: {self.RAM}')
        print(f'Motherboard: {self.motherboard}')
        print(f'Power Supply: {self.PSU}')
        print(f'Storage: {self.strorage}')

class Car:
    SPEED_LIMIT_KM: float = 360 # shared by the entire class
    
    def __init__(self, name:str,model:str,colour:str,HP:int, *,top_speed: float) -> None:
        self.name = name #only used with an instance of the class
        self.model = model # 
        self.colour = colour # 
        self.HP = HP # 
        self.top_speed = top_speed # 
        
    def drive(self) -> None:   
        print(f'{self.name} {self.model}')
        print(f'{self.HP}hp, Top speed: {self.top_speed}Km/h')
        print(f'Colour: {self.colour}')
        print(' ')
        
        if self.top_speed > self.SPEED_LIMIT_KM:
            print(f'Limiter activated: Driving at {self.SPEED_LIMIT_KM}Km , this is in the speed limit of {self.SPEED_LIMIT_KM}')
        else:
            print(f'Driving at {self.top_speed}Km')

def main():
    Audi:Car = Car('Audi','RS6 Avant','Black',600,top_speed=320)
    Audi.drive()
    
if __name__ == '__main__':
    main()    