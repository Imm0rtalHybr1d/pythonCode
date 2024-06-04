import random as r

def get_level() -> int:
    while True:    
        user_level = input('Level: ')
        try:
            user_level = int(user_level)            
            if user_level not in [1,2,3]:
                raise ValueError
            else:
                return user_level
        except ValueError:    
            continue  
        
            
def generate_integer(level): 
    while True:    
        x = r.randint(0,10)
        y = r.randint(0,10)
        try:
            check_ans(x,y)
        except ValueError:
            continue    
    
    
def check_ans(x,y) -> int:
    wrong_attempts:int = 0
    actual_ans = x+y
    score = 0
    total_attempts = 0
    
    while True:
        
        #promt user for answer
        user_ans  = input(f'{x} + {y} = ')
        try:
            #make sure user enters a number
            user_ans = int(user_ans)
            if total_attempts < 10:
                #if user enters correct answer 
                if user_ans == actual_ans:
                    score+=1 #increment the score and move to next sum
                    total_attempts +=1 #round + 1
                    
                
                #if user enteres incorrect answer
                elif user_ans != actual_ans:
                    wrong_attempts+=1  #wrong counter increments 
                    if wrong_attempts == 3: #if wrong count = 3 then print answer and move to next question 
                        print('EEE')
                        print(f'{x} + {y} = {actual_ans}')
                        total_attempts +=1  
                        continue                
                    print('EEE')
                    continue
            else:
                print(f'Total: {score} out of 10')    
                break
        except ValueError:
                continue

    
level = get_level()    
generate_integer(level)
    