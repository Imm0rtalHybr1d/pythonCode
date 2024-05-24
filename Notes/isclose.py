from math import isclose

 
#if we want to really see how accuralty close 2 floats are , we can import isclose() from math module
a: float = 9.4
b: float = 9.5

#in some cases we can say .99 is the same as 1 - 
# in python this isnt true but we can use the isclose() function to change that
print(f'{a} == {b}?' , isclose(a,b, rel_tol=.1))
#absolute tolerence lets us define by how much a float can differ 
# and still be considered the same 

def change_num():
    print(a)
    a = 123
    print( a)
    
change_num()    