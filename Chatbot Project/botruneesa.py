import sys
from isort import stream
import requests
import random
from datetime import datetime
import BTC_Class
import os
import time
def greeting(user_name:str) -> None:
    
    print('')
    print('Chatbot is typing ...')    
    time.sleep(2)
    print(f'Its a pleasure to meet you {user_name}!')
    print('')
    time.sleep(2)
    os.system('cls')
    print("Heres a list of what I can do:")
    
    print('')
    print("  * Tell you the date and time")
    print("  * Get the prices of Bitcoin (BTC)")
    print("  * Give you today's weather")
    print("  * Give you Music reccomendations on your fav artist")
    print('')
    
    print("\nHeres also a list of things I cannot do so dont bother asking:")
    print("  * Answer complex questions or engage in conversation")
    print("  * Access or control your devices")
    print("  * Perform any actions in the real world")
    print("  * Tell you if im a CHATBOT with a billion pre-defined if statements called algorythms")
    print('')

def get_user_name() -> str:
    return input('Whats your name? ')  

def get_date_time() -> str:
    #gets today date
    today = datetime.today()     
    #formats it in dd/mm/yy
    formatted_date = today.strftime("%d-%m-%Y")
    return formatted_date  # Output:  

 
    
def main():
    print(f'Hello, im a simple ChatBot with limited functionality')
    user_name:str = get_user_name()
    greeting(user_name) #greet user by their name
    
    
    while True:
        user_input = input('Ask me something >>>')
        
        if user_input.lower() in ['btc', 'bitcoin']  :
            print('Here a the currency that : ')
            print('Currency: USD, EUR, ZAR') 
            
            #prompt user to select currency
            user_currency:str = input('Please choose one of the 3 >>> ')
            
            #promt user for quantity
            BTC_quantity:float = input('Please enter a quantity >>> ')
            
            crypto: BTC_Class.BitcoinAPI = BTC_Class.BitcoinAPI(user_currency,BTC_quantity)
            crypto.connect_API()
            break
        else:
            print(f'I dont understand {user_input}')    
            continue
        
 
if __name__ == "__main__":
    main()
     