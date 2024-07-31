class computer:
    def __init__(self, CPU, GPU, RAM, Storage, Motherboard ) -> None:
        self.CPU = CPU
        self.GPU = GPU
        self.RAM = RAM
        self.Storage = Storage
        self.Motherboard = Motherboard
        
    def pc_description(self) -> None:
        print(f'{'_':_^10}PC Specifications {'_':_^10}')    
        print(f'CPU: {self.CPU}')
        print(f'GPU: {self.GPU}')
        print(f'RAM: {self.RAM}')
        print(f'Storage: {self.Storage}')
        print(f'Motherboard: {self.Motherboard}')
        print('')