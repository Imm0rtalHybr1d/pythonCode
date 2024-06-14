import random as r


while True:
    user_level = input("Level: ")
    try:
        user_level = int(user_level)
        if user_level > 0:
            break
        else:
            continue    
    except ValueError:
        continue
    

 
        
while True:
    while True:
        user_guess = input("Guess: ")
        try:
            user_guess = int(user_guess)
            if user_guess > 0:
                break
            else:
                continue    
        except ValueError:
            continue    
    try:
        if user_level and user_guess > 0: #if user level a negative number then repromt
            rand_ans = r.randint(1,user_level)
            if user_guess == rand_ans:
                print('Just right' )
                break
            elif user_guess > rand_ans:
                print('Too large')  
            elif user_guess < rand_ans:
                print('Too small')    
        else:
            continue     #reprompt user if they enter negative number      
    except ValueError:
        continue   
        
    