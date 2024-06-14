import os

os.system('cls')
elements :list[int] = [[1,2,3],3,4,5]
#use * in print to print out each element 
print(elements[0],1,2,True)
#this will output 1 2 3 1 2 True as opposed to the default -> [1,2,3],1,2,Tue
print(f'')
# ENUMARATE
enumaration: enumerate = enumerate(elements)
print(list(enumaration))
print(f'')
#we can also specify where the enumarate index should start by using the start keyword
for index,element in enumerate(elements,start=1):
    print(f'{index} is the postision & {element} is the value of that index')
    print(f'')

    
