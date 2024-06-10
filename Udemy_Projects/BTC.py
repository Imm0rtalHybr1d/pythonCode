import sys
import requests

all_currency:dict[str] = {
    '$':'USD',
    '€':'EUR',
    'R':'ZAR',
}

def converter(user_currency:str) -> None : 
    
    key:str = [key for key,val in all_currency.items() if val == user_currency]
    try:
        if user_currency == 'ZAR':
            rate = float(1347420.63)
            print(f'Current price of BTC: {key[0]}{rate:,.2f}')
            print(f'{round(quantity,0)} BTC would cost you {key[0]}{(rate*quantity):,.4f}')
        else:    
            rate = float(o['bpi'][user_currency]['rate'].replace(",", ""))#converts rate to a float by removing the comma
            print(f'Current price of BTC: {key[0]}{rate:,.2f}')
            print(f'{round(quantity,0)} BTC would cost you {key[0]}{(rate*quantity):,.4f}')
        
    except ValueError as e:
        print(e)
        


print('USD, EUR, ZAR') 



while True:
    user_currency:str = input('Currencey: ').upper()
    try:
        while True:
            if user_currency in  all_currency.values():
                quantity:int = input('Quantity: ')
                try:
                    quantity = float(quantity) 
                    if quantity > 0:              
                                           
                        #gets the JSON file from the API         
                        response =  requests.get(f'https://api.coindesk.com/v1/bpi/currentprice.json')
                        o = response.json()#stores the JSON file data in this variable  
                        converter(user_currency)
                        break
                except ValueError as e:
                    print(f'{quantity} cannot be convertered to a decimal') 
                    #reprompt 
                    continue 
            else:
                print('For now just choose between USD,EUR and ZAR')    
                break 
        break    
    except (KeyboardInterrupt,EOFError):    
        sys.exit()
        
 