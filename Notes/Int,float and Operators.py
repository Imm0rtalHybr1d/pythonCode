# ____________________INT__________________________
age : int = 30
money : int = 100
test :int = -45

#can use math operators with ints 
print(age + money)
print(age / money)
print(age - money)
print(age * money)
#int can be converted to float 
 
# __________________FLOAT____________________________
percent: float = 0.5
height: float = 1.72
width: float = 23.2333

#can use math operators with Float 
print(percent + height)
print(width / percent)
#float cannot be easily converted to int ( 10.2 -> int would yield an error without rounding the number up)
     
     
     #________________________COMPARING FLOATS ________________________________
... ;       print(f'.1 + .2 = {.1 + .2}')
    
#___________________________OPERATORS_______________________________
# // # Floor devision - this prints a divided by b but cuts it by the decimal and only gives us the whole number
# ** # Exponetional
# %  # Modulous - returns the remainder  (works opposite of floor devision)
# -
# +
# /


a:int = 10
b: int = 12
#we use floor devision opoerator
c = a // b
print(c)  # this prints 0

#ASSIGMENT OPERATORS
x: int = 2
x +=2  # this is the same as x= x + 2
x -=2  # this is the same as x= x - 2
x /=2  # this is the same as x= x / 2
x //=2
x **=2


# COMPARISON OPRATORS (returns boolean true or false)
# == Equality operator 
# != exclimation meants not , so not equal to 
# >
# <
a:int = 10
b:int = 23
c:int = 12

a == b # we check if a is equal to b 
# you can chain operators
print(a > b < c)


#LOGICAL OPERATORS - AND,OR NOT
print(a <b and b > c)
print(a <b and b > c)
print(not (a > b)) #checks if a is not more than b


#CONDITIONAL OPERATORS - always returns bool
#defining a function that captures user's expression,
# does a calculation based on the operator the user choose and then returns the answer 
def calculator(x,y,z):

    
    if y == '+': #if y = '+' is True then return x + y
         return  x + z
    elif operator == '-':
        return x - z
    elif operator == '*':
        return x*z
    elif operator == '/':
        if z != 0:
            return x/z
        else:
            return "Cannot divide by zero"
    else:
        return "Please enter a valid operator"   

    
#storing user's input in a variable 
usersExpression = input('Enter an expression: ')
numb1, operator, numb2 = usersExpression.split('/')
numb1 = float(numb1)
numb2 = float(numb2)

print(calculator(numb1,operator,numb2))




