import random
from datetime import datetime
import sys

class ChatBot:
    def __init__(self, name:str,age:str) -> None:
        self.name = name
        self.age = age
        
    def get_description(self) -> str:
        return f'{self.name} who is {self.age}'
    
    def get_responses(self, text:str) -> str: #a method that takes the user input and answers accordingly
        lowered: str = text.lower()
        
        songs = [
            "Bohemian Rhapsody - Queen",
            "A Sky Full of Stars - Coldplay",
            "Can't Stop the Feeling! - Justin Timberlake",
            "Thinking Out Loud - Ed Sheeran",
            "Perfect - Ed Sheeran",
            "Happy - Pharrell Williams",
            "Uptown Funk - Mark Ronson ft. Bruno Mars",
            "Rolling in the Deep - Adele",
            "Don't Stop Believin' - Journey",
            "I Will Survive - Gloria Gaynor"
            ]
        
        jokes:list[str] = [
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "What do you call a fish with no eyes? Fsh!",
            "What do you call a lazy kangaroo? Pouch potato.",
            "Did you hear about the restaurant on the moon? Great food, no atmosphere.",
            "A man walks into a library and asks the librarian for books about paranoia. The librarian whispers, 'They're right behind you!'",
            "What do you call a bear with no teeth? A gummy bear!",
            "Why did the bicycle fall over? Because it was two tired.",
            "Why did the golfer wear two pairs of pants? In case he got a hole in one!",
            # We'll repeat jokes 5 and 9 to ensure there are 10 unique entries. 
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "What do you call a lazy kangaroo? Pouch potato."
        ]
        
        if 'hello' in lowered:
            return f'{self.name}: Hey there!'
        elif 'bye' in lowered:
            return f'{self.name}: See you!'
        elif 'how old are you' in lowered:
            return f'{self.name}: I am {self.age} years old'
        elif 'time' in lowered:
            now: datetime = datetime.now()
            return f'{self.name}: The current time is {now:%H:%M:%S}'
        elif 'bored' in lowered:
            return f"{self.name}: I hear counting sheep works, but if you're looking for something more exciting, I'm always up for a chat! What are you interested in?"
        elif 'favorite color' in lowered:
            return f"{self.name}: Ooh, that's a tough one! I like shades that reflect the ever-changing nature of information, like Blue and Green."
        elif 'meaning of life' in lowered:
            return f"{self.name}: That's a deep question! While I don't have all the answers, I can help you search the web for some philosophical insights. What keywords would you like me to use?"
        elif 'secret' in lowered:
            return f"{self.name}: Woah, you found the secret code! You've unlocked a special message: {'You a Busta'}"  # Replace with your secret message
        elif 'congratulations' in lowered:
            return f"{self.name}: Woohoo! Happy to hear it! "
        
        elif 'tell me a joke' in lowered:
            # Access and store a list of jokes beforehand
            return f"{self.name}: {random.choice(jokes)}"  # Replace with your jokes list

        elif 'songs' in lowered:
            # Access and store a list of genres or artists
            return f"{self.name}: Need some tunes? How about {random.choice(songs)} or {random.choice(songs)}?"

        elif 'movie recommendations' in lowered:
            # Access and store a list of genres or popular movies
            return f"{self.name}: In the mood for a movie? How about a {random.choice([
                                "A Hidden Gem",
                                "Nostalgia Trip",
                                "Mind-Bending Thriller",
                                "Foreign Flair",
                                "Cult Classic"
                            ])}"

        elif 'compliment' in lowered:
            # Access and store a list of compliments
            return f"{self.name}: You seem like a really {random.choice(["That project you're working on sounds really impressive! Your dedication is inspiring.","Your ideas are always so fresh and creative! It's a joy to see your unique perspective.","You have such a kind heart. The way you treat others is truly heartwarming.", "You're a natural at problem-solving! Your ability to think critically is amazing."])} person! "

        elif 'headlines' in lowered:
            # Access and store a function to safely retrieve news headlines (avoid external links)
            return f"{self.name}: Want to stay informed? Here are some headlines: {'Youre Gay , you a Gaya, your momy name AUnty GAYA and your dady name GAYbrial , how do you feel GAYbriel jr , tell me lil nigga'}"

        elif 'word of the day' in lowered:
            # Access and store a function to safely retrieve a word of the day (avoid external links)
            return f"{self.name}: Expand your vocabulary! Today's word of the day is '{'Poes'}'. Can you use it in a sentence?"

        # Expressing Emotions and Opinions (avoiding sensitive topics)

        elif 'happy' in lowered:
            return f"{self.name}: That's awesome to hear! Spread the positivity! "

        elif 'sad' in lowered:
            return f"{self.name}: Aw, that's tough. Sometimes talking it out helps. Here to listen if you want to chat. "

        elif 'frustrated' in lowered:
            return f"{self.name}: I understand feeling frustrated. Take a deep breath and let's see if we can work through it together. "

        # Encouraging Interaction and Learning

        elif 'teach me something' in lowered:
            return f"{self.name}: I'm always learning too! What would you like to teach me?"

        elif 'learned something' in lowered:
            learned_something = lowered.split('that')[1].strip()
            return f"{self.name}: That's interesting! Thanks for sharing, I'm always learning new things. "

        # Lighthearted Responses

        elif 'hello' in lowered:
            greetings = ['Hey there!', 'Hi!', 'What\'s up?']
            return f"{self.name}: {random.choice(greetings)}"

        elif 'bye' in lowered:
            farewells = ['See you!', 'Have a great day!', 'Talk to you later!']
            return f"{self.name}: {random.choice(farewells)}"

        elif 'thanks' in lowered:
            return f"{self.name}: You're welcome! "

        # Placeholder Responses (avoid making claims of sentience or consciousness)

        elif 'who are you' in lowered:
            return f"{self.name}: I'm a large language model, here to help you with ... you know what , nevermind"
        elif 'angry' in lowered:
            return f"{self.name}: I understand you might be feeling angry.  Would you like to talk about it, or would you prefer to try a calming activity?"
        else:
            return f"{self.name}: I'm sorry, I don't quite understand.  Could you rephrase that, or try asking something different?"

    def run(self) ->None:
        while True:
            user_input: str = input('You: ')
            if user_input == 'exit':
                sys.exit('Thanks for chatting')
                
            else :
                response:str = self.get_responses(user_input)
                print(response)
 
class Dog(ChatBot): #created a Dog class which can inheret from CHatBot class
    def __init__(self,name:str,breed:str, age:str) -> None:
        self.name = name
        self.breed = breed
        self.age = age
        super().__init__(name,age)
                      
def main():
    # mario: ChatBot = ChatBot('Basic ass chat bot', '1 day old bitch')           
    # mario.run() 
    
    dog: Dog = Dog('Lola','Pitbul & Boerbull','6 months')
    print(dog.get_description())

main()
