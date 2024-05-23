def greet(name:str, language:str , default='Hello') -> str:   #when we define a function we can also specify its parameters
    if language == 'afrikaans':
        print(f'Goeie Dag {name}')
    elif language == 'german':
        print(f'Hallo, {name}')  
    else:
        print(f'{default}, {name}')      



user_input =(input('Enter your name and language: '))    #when we use the function we pass in an argument
name, language = user_input.split(' ')
greet(name,language) 