import os
os.system('cls')

for num in range(1,10):
    print(num,end=' ')    
print('')

# ____ using RANGE CLASS____
my_range:range = range(0,10)

print(list(my_range))
print('')

my_range:range = range(0,-10, -2)
print(list(my_range))