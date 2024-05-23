import string

def check_input(user_input:str) -> True:      
    
    alphabet :str = string.ascii_letters+' '
    
    for char in user_input:
        if char not in alphabet:
            raise ValueError ('Not all the characters in your input are string')
    print(f'All the characters in your input are string')    
               
def main ()-> None:
    while True:
        try:
            user_input: str = input('Check Text: ')
            check_input(user_input)
            print('')            
        except ValueError:
            print(f'Only enter letters!, {user_input} is not letters only')
            continue
        except Exception as e:
            print(f'Error: P{type(e)}{e}')  
            continue  
main()              