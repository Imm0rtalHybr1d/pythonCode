class Car:
    def __init__(self,brand,model,colour,top_speed,v_type) -> None:
        self.brand = brand
        self.model = model
        self.colour = colour
        self.top_speed = top_speed
        self.v_type = v_type
        
    def display_car(self) -> None:
        print(f'{'_':_^10}Car Specifications {'_':_^10}')    
        print(f'Brand: {self.brand}')
        print(f'Model: {self.model}')
        print(f'Colour: {self.colour}')
        print(f'Top Speed: {self.top_speed}')
        print(f'Vehicle Type: {self.v_type}')
        print(f'{''}')