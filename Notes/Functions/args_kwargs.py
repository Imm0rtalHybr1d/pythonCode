# *ARGS_____________WILL ALWAYS CONVERT TO TUPPLE__________________________________
# *args - refers to the arguments , **kwargs refers to keyword arguments

#this function takes in args of type int and returns int
def add(*args:int) -> int: 
    print(args)
    return sum(args)

print(add(1,2,3))

#creates a function that takes in *args called people,
# a positional arg called greeting 
#and another arg called ending 
def greet(*people:str,greeting:str,ending:str) -> None:
    #passing multiple values into *args creates a tupple by default
    #we then use a for loop to iterate over through the tupple
    for person in people: 
        print(f'{greeting} {person}, {ending}')
greet('Hano','Hiemie','Nueeb',greeting='Hello',ending='we gyming today? ') 

# *KWARGS___________WILL ALWAYS CONVERT TO DICT_________________________
def pin_position(**kwargs: int) -> None:
    print(kwargs)
    
pin_position(x=10,y=20)    