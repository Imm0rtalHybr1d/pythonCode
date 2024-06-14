import emoji as e

def emojize_by_name(emoji_name:str) -> None :
    emoji = e.emojize(emoji_name)
    if e.is_emoji(emoji):
        print(emoji)
    else:
        print("Please use a valid emoji name")        

def emojize_by_alias(emoji_name:str)-> None :
    emoji = e.emojize(emoji_name, language='alias') #tries to emojize it 
    if e.is_emoji(emoji): #returns true if user string was emjized
       print(emoji)
    else:
        print("Please use a valid emoji name")   

def valid_emoji_name(emoji_name:str) -> bool:
    return emoji_name.startswith(":") and emoji_name.endswith(':') 


while True:
    user_input = input("Please enter an emoji name such as ':thumbs_up:' >>> ")  
    try: #try to split 
       
        ui = user_input.split(',')
        
        if  valid_emoji_name(ui[1].strip()) :
            if '_' in ui[1]:
                emojize_by_name(ui[1].strip())
                break
        else:
            emojize_by_alias(ui[1].strip())
            break
        
    except IndexError:        
        if  valid_emoji_name(user_input.strip()) :
            if '_' in user_input:
                emojize_by_name(user_input.strip())
                break
            else:
                emojize_by_alias(user_input.strip())
                break
        else:
            print('Enter a valid emoji name')            
        
        
