import sys
import random
from datetime import datetime

# Dictionary of languages and their corresponding "Hello" translations
greetings: dict[str] = {
    "english": "Hello",
    "afrikaans": "Hallo",
    "spanish": "Hola",
    "french": "Bonjour",
    "german": "Hallo",
    "italian": "Ciao",
    "japanese": "こんにちは (Konnichiwa)",
    "chinese": "你好 (Nǐ hǎo)",
    "russian": "Здравствуйте (Zdravstvuyte)",
    "arabic": "مرحبا (Marhaban)",
    "hindi": "नमस्ते (Namaste)",
    "portuguese": "Olá",
    "korean": "안녕하세요 (Annyeonghaseyo)",
    "swedish": "Hej",
    "dutch": "Hallo",
    "turkish": "Merhaba",
    "greek": "Γειά σου (Geia sou)",
    "thai": "สวัสดี (Sawasdee)",
    "polish": "Cześć",
    "hebrew": "שלום (Shalom)",
    "finnish": "Hei",
    "norwegian": "Hallo",
    "hungarian": "Szia",
    "czech": "Ahoj",
    "danish": "Hej",
    "swahili": "Hujambo",
    "vietnamese": "Xin chào",
    "malay": "Halo",
    "indonesian": "Halo",
    "filipino": "Kamusta",
    "romanian": "Salut"
}

#dictionaries containt goodbye greetings in diffrent languages
goodbye: dict[str] = {
    "english": "Goodbye",
    "spanish": "Adiós",
    "french": "Au revoir",
    "german": "Auf Wiedersehen",
    "italian": "Arrivederci",
    "japanese": "さようなら (Sayonara)",
    "chinese": "再见 (Zàijiàn)",
    "russian": "До свидания (Do svidaniya)",
    "arabic": "مع السلامة (Ma'a as-salama)",
    "hindi": "अलविदा (Alvida)",
    "portuguese": "Adeus",
    "korean": "안녕히 가세요 (Annyeonghi gaseyo)",
    "swedish": "Adjö",
    "dutch": "Vaarwel",
    "turkish": "Hoşçakal",
    "greek": "Αντίο (Antio)",
    "thai": "ลาก่อน (Laa k̀xn)",
    "polish": "Do widzenia",
    "hebrew": "להתראות (Lehitraot)",
    "finnish": "Näkemiin",
    "norwegian": "Farvel",
    "hungarian": "Viszlát",
    "czech": "Sbohem",
    "danish": "Farvel",
    "swahili": "Kwaheri",
    "vietnamese": "Tạm biệt",
    "malay": "Selamat tinggal",
    "indonesian": "Selamat tinggal",
    "filipino": "Paalam",
    "romanian": "La revedere"}

#if user asks how are you 
how_are_you: list[str] = ["I'm on top of the world! How about you?",
"Feeling fantastic, thanks for asking! How are you?",
"Living the dream! How's everything on your end?",
"Couldn't be better! How about yourself?",
"Just peachy, how about you?",
"I'm doing splendidly, how's it going with you?",
"Feeling amazing, how are you?",
"I'm fantastic, thank you, how are you?",
"I'm great, riding the wave of life, how about you?",
"Absolutely fabulous, how are you?",
"I'm doing wonderfully, how are you?",
"I'm in high spirits, how are you?",
"Better than a double rainbow, how are you?",
"I'm rocking and rolling, how are you?",
"All good here, how are things on your side?",
"Couldn't be happier, how's everything with you?",
"I'm as happy as a clam, how are you?",
"Doing well and feeling swell, how are you?",
"I'm over the moon, how are you?",
"Life's good, how about you?",
"I'm stellar, thanks for asking, how are you?",
"I'm on cloud nine, how are you?",
"Feeling tip-top, how about you?",
"I'm chipper, thanks, how are you?",
]


def greet_user(user_lang:str,user_name:str) -> str:    
    print(f'{greetings[user_lang]} {user_name}')
                 
def get_response(user_lang,username) -> str:
    
    while True:
        try:
            lowered = input('You: ').lower()
            if 'how are you' in lowered:
                print(f'BOT: {random.choice(how_are_you)}')
                u_input = input()
                print(f'BOT: Im glad to hear that :)')
                continue
            elif 'time' in lowered:
                current_time = datetime.now()    
                print(f'BOT: The current time is {current_time:%H:%M}')
                continue
            elif 'date' in lowered:
                current_date = datetime.today()
                print(f'BOT: Today\'s date is {current_date:%d %B %Y}')
                continue
            else:
                print(f'BOT: Im a simple bot, ask me simple things like the date or time')
                continue
        except(EOFError,KeyboardInterrupt,KeyError):
            print('')
            print(f'BOT: {goodbye[user_lang]}, {username} ')
            sys.exit()

def check_lang (user_lang):
    #check laguages 
    if user_lang in greetings and goodbye:
        greet_user(user_lang) 
    else :
        print('BOT:I dont know that language, try another :(')    

def main():
    print('BOT: what is your name ? ')
    #get user name
    user_name = input('You: ')
    print(f'BOT: What language would you like to be greeted in ? ' ) 
    #get user language
    user_lang = input(f'You: ').lower()

    check_lang(user_lang) 
    get_response(user_lang,user_name) 
    
if __name__ == '__main__'   :
    main()