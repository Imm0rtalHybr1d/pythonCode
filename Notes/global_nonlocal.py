#________________________GLOBAL_________________
a = 66
def change_num():
    global a
    print(a)
    a = 123
    b = 546
    print( a)
change_num()    
    
#______________NON LOCAL__________________    
def outer_func() -> None: 
    name: str = ''
    value: int = 0
     
    def inner_func():
        nonlocal name,value
        name = 'Tommo'
        value = 12
    
    inner_func() 
    print(name, value)  
    
     
