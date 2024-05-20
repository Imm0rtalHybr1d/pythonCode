def get_length(text:str) -> int:
    print(f'Getting the length of: "{text}"')
    return len(text)
print(get_length(text='Hano'))
    
def make_upper(name:str) ->str:
    print(f'making to upper')
    return name.upper()
print(make_upper())


def main():
    print('enter a number')
    xx = input()
    
    print(mulitplyInput(xx))
    
def mulitplyInput (inte):
    z = int(inte) * int(2)
    return z 


main()