from os import system

system('cls')

#_______GLOBALS()_____________________
#prints the dictionary containing the current scope's global variables.
print(f'{globals()}')
print(f'')

#creating a dict and storing the dict object that globals() returns in the dictionary 
globals_dict:dict[str:any] = dict(globals())

for k,v in globals_dict.items():
    print(f'{k}: {v}')
    
system('cls')    
#_______________LOCALS()_____________________    
def add(a:int,b:int) -> None:
    result = a + b
    print(f'{a} + {b} = {result}')
    
    print(f'add() has: {locals()}')
    
    local:dict = dict(locals())
    for k,v in local.items():
        print(f'Key:{k}, Value:{v}')
    
add(1,2)    