import os

os.system('cls')
a:float = 32.27522222
b:float = 55.222222522
c:float = 32.2222222

#_____ROUNDING OFF NUMBERS____________

answer:float = sum([a,b,c])
print('')
print(f'{round(answer,2)}')
print('')
print(f'{round(answer,1)}')
print('')
print(f'{round(answer,0)}')
print('')
#using -1 as the round value , will round off to the nearest 10th 
#e.g 106 will round off to 110
print(f'{round(answer,-1)}')
print('')

#using -1 as the round value , will round off to the nearest 100th 
#e.g 106 will round off to 100
print(f'{round(answer,-2)}')