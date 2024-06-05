import random as r
from pyfiglet import Figlet

f= Figlet(font='slant')



def get_level() -> int: #make sure user level is in list[1,2,3]
    while True: #loop that will constant ask level if user doesnt enter 1,2,3
        chosen_level  = input('Level: ')
        try:
            chosen_level = int(chosen_level)
            if chosen_level  in [1,2,3]:
                return chosen_level #returns the level
            else:
                raise ValueError 
        except ValueError:
            continue    

def generate_rand(level:int) -> tuple:
    """Generates a random number range based on the level."""
    min_val = r.randint(1,(10* level)) 
    max_val = r.randint(10,(20* level))
    return min_val,max_val  

def play_game() -> None:
    
    score:int = 0
    wrong_counter = 0
    round_count = 1 
    
    print(f.renderText(f'Start : '))
    
    """Main game loop that handles rounds and scoring."""
    while round_count < 11:
        x,y = generate_rand(user_level) 
        actual_answer = x+y
        while True:
            print('---------')
            #prints the text in FIGLET
            
            
            
            print((f'Round: {round_count}'))
            print('---------')
            user_answer = input(f'{x} + {y} = ')
            try:
                user_answer = int(user_answer)  #make sure user enteres an int                
                #user enters correct answer 
                if user_answer == actual_answer: 
                    score+=1
                    round_count+=1
                    break
                    
                else:
                    if wrong_counter == 2:
                        print('EEE')
                        print(f'the answer is: {actual_answer}')
                        round_count+=1
                        break
                    print('EEE')
                    wrong_counter +=1
                    continue
            except ValueError:
                ...           
                 
    print(f'Total: {score} out of 10')

if __name__ == '__main__':
    user_level = get_level()   #calls func that gets the level   
    play_game()
