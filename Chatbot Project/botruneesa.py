import sys
import random
from datetime import datetime
import BTC_Class
import Itunes_Class
import Weather_Class
import os
import time 

os.system('cls')
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
    print("  * Tell you the date and time - Date")
    print("  * Get the prices of Bitcoin (BTC) - BTC")
    print("  * Give you today's weather - Weather")
    print("  * Give you Music reccomendations on your fav artist - Music")
    print('')
    
    print("\nHeres also a list of things I cannot do so dont bother asking:")
    print("  * Answer complex questions or engage in conversation")
    print("  * Access or control your devices")
    print("  * Perform any actions in the real world")
    print("  * Tell you if im a CHATBOT with a billion pre-defined if statements called algorithm")
    print('')

def get_date_time() -> None:
    #gets today date
    today = datetime.today()     
    #formats it in dd/mm/yy
    formatted_date = today.strftime("%d %B %Y")
    print(f'Todays date is {formatted_date}')  
        
def main():
    os.system('cls')
    print(f'Hello, im a simple ChatBot with limited functionality')
    user_name:str = input('Whats your name? ')  #prompt user for their name
    greeting(user_name) #greet user by their name
    
    while True:
        user_input = input('Ask me something >>> ')
        
        if user_input.lower() in ['btc', 'bitcoin']  :
            print('')
            print('Choose a currency: USD, EUR, ZAR') 
            
            #prompt user to select currency
            user_currency:str = input('Please choose one of the 3 >>> ')
            
            #promt user for quantity
            BTC_quantity:float = input('Please enter a quantity >>> ')
            
            crypto: BTC_Class.BitcoinAPI = BTC_Class.BitcoinAPI(user_currency,BTC_quantity)
            crypto.connect_API()
            break
        elif 'date' in user_input.lower():
            get_date_time()
            
        elif 'weather' in user_input.lower():
            user_city:str = input('Please enter the name of your city ')
            os.system('cls')
            
            weather: Weather_Class.Weather = Weather_Class.Weather(user_city)
            weather.get_weather()
        
        elif 'music' in user_input.lower():
            user_artist: str = input('Please enter an artist name >>> ')
            user_query:str = input('Would you like to view songs or albums of this artist >>>')
            
            if user_query.lower() in ['song','songs']:
                user_num_of_songs:int = input('Please enter the number of songs reccomendations youd like >>> ')
                itunes:Itunes_Class.Itunes_API = Itunes_Class.Itunes_API(user_artist)            
                itunes.get_songs(user_num_of_songs)
            elif user_query.lower() in ['album', 'albums']:
                itunes:Itunes_Class.Itunes_API = Itunes_Class.Itunes_API(user_artist)            
                itunes.get_albums()
                
            print('')
        else:
            print(f'I dont understand {user_input}')  
            print('Thers a reason my name is Botruneesa') 
            continue
        
 
if __name__ == "__main__":
    main()
     