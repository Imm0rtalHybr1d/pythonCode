import random
from typing import final

AUTHOR: final = 'Mr Martin'
VERSION: final = 1

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
rand_list: list[str]= []

def greet(name:str) -> None:
    for k,v in greetings.items():
        rand_list.append(v)
    rand_item = random.choice(rand_list)
    print(f'{rand_item}, {name}')    



