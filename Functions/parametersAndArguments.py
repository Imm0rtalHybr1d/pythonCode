def greet(name:str) -> str:   #when we define a function we can also specify its parameters
    print(f'Hello {name}')

greet(input('Enter your name: '))    #when we use the function we pass in an argument