from dataclasses import dataclass

@dataclass
class Fruit:
    name:str
    grams:float
    price_per_kg:float
    
    """In Python, @property is a decorator that lets you create "calculated attributes" in your classes. 
    These attributes are not stored directly but are calculated on demand."""
    def describe(self) -> None:
        print(f'{self.grams}g of {self.name} costs R{self.total_price}')
        
    @property
    def total_price(self) -> float:
        return (self.grams/1000) * self.price_per_kg
    
    @property
    def price_inflated(self) -> float:
        return self.total_price * 1.5
        
def main():
    apple: Fruit = Fruit('Apple', 100, 5)
    pear: Fruit = Fruit('Pear', 90, 10)
    
    print(f'{apple}')
    print(f'{apple.describe()}')
    print(f'{''}')    
    apple.price_per_kg = 20
    print(f'{apple}')
    print(f'{apple.describe()}')
    print(f'Inflated Price for apples: R{apple.price_inflated}')

if __name__ == "__main__":
    main()
     