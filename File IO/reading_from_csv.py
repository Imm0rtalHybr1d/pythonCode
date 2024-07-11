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
    students:dict[str:str] = {}
    
    for row in rows:
        #unpacking key and value from each line in csv file 
        #unpacked into 2 viariables serperated by the comma 
        name,surname = row.rstrip().split(',')
        
        #assigned the values of name and surname to the name and surname keys of the
        students['name'] = name
        students['surname'] = surname

        print(f'{students['name']}, {students['surname']}')   

       