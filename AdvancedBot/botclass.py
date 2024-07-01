from difflib import get_close_matches

class Botclass:
    brain:dict[str:str] = {'Hello':'Hey there!',
                           'How are you':'Im great thanks!',
                           'blah':'blah blah',}
    
    def __init__(self,user_question:str) -> None:
        self.user_question = user_question
    
    #purpose of this function is to find the best match of the question the user asks
    def get_best_match(self) -> str|None:  
        #stores each question from the dictionary into a list 
        self.questions: list[str] = [q for q in self.brain]
    
        #then compares if the user's question is in the list of questions using the getclosematches()
        self.matches:list[str] = get_close_matches(self.user_question, self.questions, n=1, cutoff=0.6)
        
        #if there are matches then return taht match else, return none 
        if self.matches:
            return self.matches[0]  
        else:
            return 'I dont understand'
        
    def run_chatbot(self) -> None:
        self.best_match:str | None = self.get_best_match()
        self.response:str = self.brain.get(self.best_match) 
        
        if self.response:
            print(f'Bot: {self.response}')    
        else:
            print(f'Bot: I dont understand')    