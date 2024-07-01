from botclass import Botclass
from os import system
            
def main():
    while True :
        user_input:str = input('You: ')
        new_bot: Botclass = Botclass(user_input)        
        new_bot.run_chatbot()
        
if __name__ == "__main__":
    system('cls')
    main()
             