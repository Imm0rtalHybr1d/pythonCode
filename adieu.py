import inflect

p = inflect.engine()
# JOIN WORDS INTO A LIST:
my_list :list[str] = []
while True:
    
    user_input = input('Name: ')
    try:
        my_list.append(user_input) 
        continue
    except (KeyError,KeyboardInterrupt,EOFError) :
        print(f'Adieu, adiue, to {p.join(my_list)}')
       