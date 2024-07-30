

def value(greeting:str) -> int:
    if greeting.startswith('hello'):
        return 0
    elif greeting.startswith('h') and greeting!= 'hello':
        return 20
    else :
        return 100

def main():
    userInput = input('Greeting: ').strip().lower()
    value(userInput)
 
if __name__ == "__main__":
    main()
 