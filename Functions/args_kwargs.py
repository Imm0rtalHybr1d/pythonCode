# *args - refers to the arguments , **kwargs refers to keyword arguments

#this function takes in args of type int and returns int
# def add(*args:int) -> int: 
#     print(args)
#     return sum(args)

# print(add(1,2,3))

#creates a function that takes in *args called people,
# a positional arg called greeting 
#and another arg called ending 
def greet(*people:str,greeting:str,ending:str) -> None:
    for person in people:
        print(f'{greeting} {person}, {ending}')
greet('Hano','Hiemie','Nueeb',greeting='Hello',ending='we gyming today? ') 