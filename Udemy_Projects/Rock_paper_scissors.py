import random
import sys
import time
#STEP 1: STARTING INFO
print('Welcome to Rock Paper Scissors! ')
print('__________________________________ ')

#store moves in a diciotnary, with words as the key and emoji as the value 
moves: dict = {
    'rock': '🪨',
    'paper': '🧻',
    'scissors': '✂️'
}

#stores the keys in a list - gets the keys using the .keys()
valid_moves: list[str] = list(moves.keys())

#Score Tracker
user_score: int = 0
ai_score: int = 0

#create a function that prints score
def print_score():
    print(f'Score') 
    print(f'Busta: {user_score} - Ai: {ai_score} ' )    
    
    
#creates a function that prints diffrent comments based on the score    
def extr_comments() -> str:
    print('')
    if user_score == 1:
        print('Nice')
    elif user_score > 2:
        print('Awww shittdd, you on a role busta')       
    elif user_score < ai_score:   
        print(f'Ai says: Keep Up Muthafucker' )
    elif user_score < ai_score and ai_score > 4:
        print('Ai is typing...')
        time.sleep(4.5)
        print('Ai says: Man yous a Busta, straight Busta')
    print('__________________________________')    

def print_moves() -> str: 
        #print the user's move
    print('-------')
    print(f'Busta: {moves[user_move]}')
    #print AI move
    print(f'AI: {moves[ai_move]}')
    print('-------')    

#STEP 2: INFINITE LOOP
while True:
    #get user input
    user_move: str = input('Rock, Paper or Scissors? >> ').lower()

    #check if user wants to keep playing , if they type in exit , then terminate the program
    if user_move == 'exit':
        print('Thanks for playing Busta! ')
        sys.exit()
        
    #check if user entered a valid move 
    if user_move not in valid_moves:
        print('Invalid move Busta ')
        continue
    
    #AI decides
    #use random.choice() to choose a random one of the moves and store it in the ai_move variable
    ai_move: str = random.choice(valid_moves)
    
    #print the user's move
    print_moves()
    
    #CHECK MOVES
    if user_move == ai_move: #tie
        print('Its a tie! ')
        print_score()
        print('__________________________________')   
        
    elif user_move == 'rock' and ai_move == 'scissors':         
        user_score+=1   
        print_score()
        extr_comments()
        
    elif user_move == 'paper' and ai_move == 'rock':
        user_score+=1 
        print_score()
        extr_comments()
        
    elif user_move == 'scissors' and ai_move == 'paper':         
        user_score+=1 
        print_score() 
        extr_comments()
        
    else:        
        ai_score+=1      
        print_score()
        extr_comments() 
                        
