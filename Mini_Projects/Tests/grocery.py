#create an empty dictionary 
user_dict :dict[str,int] = {}

#create a while loop that constantly prompts
while True:
    
    user_input = input('Enter fruit name: ')
    try:
        
        if user_input in  user_dict:
            user_dict[user_input] += 1
        else:   
            user_dict[user_input] = 1
            
    except (EOFError,KeyboardInterrupt,KeyboardInterrupt,KeyError):
        
        print('')
        break

# new_dict = sorted( user_dict.items)
for k,v in sorted(user_dict.items()):
    print(f'{v} {k.upper()}')
