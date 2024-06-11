import sys
import requests


class BitcoinAPI:
    all_currency = {
            '$':'USD',
            '€':'EUR',
            'R':'ZAR',
        }
    def __init__(self,user_currency:str,quantity:str) -> None:
        self.user_currency = user_currency
        self.quantity = quantity

        self.all_currency = {
            '$':'USD',
            '€':'EUR',
            'R':'ZAR',
        }
        
    def test(self):
        print('Hi BTC')
        
        
    def get_BTC_price(self) ->str:
        self.key:str = [self.key for self.key,self.val in self.all_currency.items() if self.val == self.user_currency]
        try:
            if self.user_currency == 'ZAR':
                rate = float(1347420.63)
                print(f'Current price of BTC: {self.key[0]}{rate:,.2f}')
                print(f'{round(self.quantity,0)} BTC would cost you {self.key[0]}{(rate*self.quantity):,.4f}')
            else:    
                rate = float(self.response['bpi'][self.user_currency]['rate'].replace(",", ""))#converts rate to a float by removing the comma
                print(f'Current price of BTC: {self.key[0]}{rate:,.2f}')
                print(f'{round(self.quantity,0)} BTC would cost you {self.key[0]}{(rate*self.quantity):,.4f}')
        except ValueError as e:
            print(e)
    
    #checks if user currency is in our dic of currencies        
    def connect_API(self):
        if self.user_currency in self.all_currency.values(): 
            try:
                self.quantity = float(self.quantity)
                if self.quantity > 0:              
                                            
                    #gets the JSON file from the API         
                    self.response =  requests.get(f'https://api.coindesk.com/v1/bpi/currentprice.json')
                    self.response = self.response.json()#stores the JSON file data in this variable  
                    self.get_BTC_price()
                else:
                    print(f'Cannot enter {self.quantity} ')    
            except ValueError:
                print(f'Cannot convert {self.quantity} to a float, please use numbers only')        
                