# *args - refers to the arguments , **kwargs refers to keyword arguments

#this function takes in args of type int and returns int
# def add(*args:int) -> int: 
#     print(args)
#     return sum(args)

# print(add(1,2,3))

#
def greet(*people:str,greeting:str,ending:str) -> None:
    for person in people:
        print(f'{greeting} {person}, {ending}')
greet('Hano','Hiemie','Nueeb',greeting='Hello',ending='we gyming today? ')