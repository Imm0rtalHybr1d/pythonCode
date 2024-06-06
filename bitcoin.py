import sys
import requests


print('This program is a simple Bitcoin price checker >>>')
currency:str = input('Please choose a currency:')
print('1 - USD')
print('2 - EUR')
print('3 - GDP')
print('4 - ZAR')
try:
    sys.argv[1]  = float(sys.argv[1])    
    #we can also ensure that user has entered the right amount of args using if len(arg[])    
    if len(sys.argv) == 2:
        #gets the JSON file from the API         
        response =  requests.get(f'https://api.coindesk.com/v1/bpi/currentprice.json')

        #stores the JSON file data in this variable    
        o = response.json()
        
        try:
            
            #converts rate to a float by removing the comma
            rate = float(o['bpi']['USD']['rate'].replace(",", ""))
            print(f'Current price of BTC: ${rate:,.4f}')
            print(f'{sys.argv[1]} BTC would cost you ${(rate*float(sys.argv[1])):,.4f}')
            # print(f'{sys.argv[1]} BTC would cost you {rate*2}')
        except ValueError as e:
            sys
    else:
        raise IndexError("Too many args")
except ValueError as e:
    sys.exit(f'Cannot convert {sys.argv[1]} to float')      
except (KeyboardInterrupt,EOFError):    
    sys.exit
 