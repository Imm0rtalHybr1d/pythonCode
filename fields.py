from dataclasses import dataclass, field

@dataclass
class Fruit:
    name:str
    grams:float
    price_per_kg:float
    #The field function is used to specify additional options for the attribute.
    edible:bool = field(default=True) # we tell python to insert true as the default value for edible 
    #not all fruit has relateable fruits, so we specify the python creates a new list by default
    related_fruits: list[str] = field(default_factory=list)
    
def main():
    apple: Fruit = Fruit('Apple', 100, 5)
    pear: Fruit = Fruit('Pear', 90, 10, related_fruits='Apple')
    
    print(f'{apple}')
    print(f'{pear}')
    print(f'Fruits related to pears: {pear.related_fruits}')
    print(f'Apple cost R{apple.price_per_kg}')    
    
 
if __name__ == "__main__":
    main()
     