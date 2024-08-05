from dataclasses import dataclass

#most common reason for using dataclasses are for its flexability, ease of use
# also easier to compare and use the data compared to regular claseses
# also if you just want create a class just to store data that you want to view and minupulate 

"""Dataclasses are a powerful feature introduced in Python 3.7.
They provide a concise and convenient way to define classes that primarily hold data.
Here's why they're so useful:"""
@dataclass
class Coin:
    name: str
    value: float
    coin_id: str
    
def main() -> None:
    bitcoin: Coin = Coin('Bitcoin', 10_000, 'BTC')
    etherium: Coin = Coin('Etherium', 9_000, 'ETH')
    ripple: Coin = Coin('Ripple', 200, 'XRP')
    
    print(bitcoin)
    print(etherium)
    print(ripple)
    
    print(f'{''}')
    
    #we can also easily compare instances of the data class
    print(bitcoin == etherium) #by default compares by value
    
 
if __name__ == "__main__":
    main()
     
