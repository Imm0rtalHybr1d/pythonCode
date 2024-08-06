from dataclasses import dataclass, field, InitVar

""" Summary

The __post_init__ method in dataclasses provides a convenient way to perform actions after the initial attribute values are set.
This is particularly useful for calculating derived attributes or performing additional initialization logic."""

@dataclass
class Fruit:
    name:str
    grams:float
    price_per_kg:float
    is_rare: InitVar[bool | None] = None # we explicitly tell python that is_rare should run with the __init__
    total_price: float = field(init=False)
    
    # Post initializer only runs once 
    def __post_init__(self, is_rare: bool | None):
        
        if is_rare:
            self.price_per_kg *= 2
        
        self.total_price = (self.grams/1000) * self.price_per_kg
        
    def describe(self) -> None:
        print(f'{self.grams}g of {self.name} costs R{self.total_price}')    
        
def main():
    apple:Fruit = Fruit('Apple', 2500, 5)
    orange:Fruit = Fruit('Orange', 3500, 10)
    passion: Fruit = Fruit('Passion Fruit', 2100, 10, is_rare=True)
    
    print(f'{apple}')
    print(f'{orange}')
    print(f'{passion}')
   
    
    
 
if __name__ == "__main__":
    main()
         