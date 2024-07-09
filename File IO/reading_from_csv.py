# This Python code is reading the contents of a file named 'testing.csv' and then processing each row.
# Here is a breakdown of what the code does:
with open('testing.csv') as file:
    rows:list[str] = file.readlines()
    
    for row in rows:
        elements = row.rstrip().split(',')
        
        print(f'•Name:{elements[0]} •Surname:{elements[1]}')
        
print(f' ')        
        
# This part of the code is creating a dictionary named `students` where the keys are strings and the
# values are also strings. For each row in the `rows` list, it splits the row into `name` and
# `surname` based on the comma delimiter. Then, it assigns the `name` to the key `'name'` in the
# `students` dictionary and the `surname` to the key `'surname'` in the `students` dictionary.

with open('testing.csv') as file:
    rows:list[str] = file.readlines()    

    for row in rows:
        name,surname = row.rstrip().split(',')
        students:dict[str:str] = {'name':name, 'surname':surname}
        
        print(f'{students['name']}, {students['surname']}')
       