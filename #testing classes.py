#testing classes


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
        
def main():
    #creating an instance of the class we created , the instance is called mp_pc
    #can also be called an objec ...an object is an instance of a class
    my_pc: PC_spec = PC_spec('Ryzen 5, 5600x', 
                            'Gigabyte RTX 3060ti',
                            '32GB DDR4',
                            'MSI Motar B550',
                            '750w Corsair',
                            '500GB NVME SSD, 500GB SATA SSD, 2TB HDD')
    my_pc.specifications()    
    
if __name__ == '__main__':
    main()    