import random as r
import pyfiglet as Figlet

figlet = Figlet()
# sets the font to the random one 
figlet.setFont(font='slant')



def get_level() -> int: #make sure user level is in list[1,2,3]
    while True: #loop that will constant ask level if user doesnt enter 1,2,3
        chosen_level  = int(input('Level: '))
        try:
            if chosen_level  in [1,2,3]:
                return chosen_level #returns the level
            else:
                raise ValueError 
        except ValueError:
            continue    

def generate_rand(level:int) -> tuple:
    min_val = r.randint(1,(10* level)) 
    max_val = r.randint(10,(20* level))
    return min_val,max_val  

def make_sum() -> None:
    #calls func that stores 2 randon numbers in a tupple
    score:int = 0
    wrong_counter = 0
    round_count = 1 
    
    
    while round_count < 11:
        rand_nums: tuple[int] = generate_rand(user_level) 
        x = rand_nums[0]
        y = rand_nums[1]
    
        actual_answer = x+y
        while True:
            print('---------')
            #prints the text in FIGLET
            print(figlet.renderText(round_count))
            print(f'Round: {round_count}')
            print('---------')
            user_answer = input(f'{x} + {y} = ')
            try:
                user_answer = int(user_answer)  
                
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
           
    
  
      
user_level = get_level()   #calls func that gets the level   
make_sum()
