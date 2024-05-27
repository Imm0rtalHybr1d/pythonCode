test : list [str] = ['hano', 'hiemie','carlo']
h_names: list[str] = [name for name in test if name.startswith('h')]
print (h_names)

# Another example
uneven :list[int] = [1,3,5,7,9]
even:list[int]= [num  #return num from for looop
                 for num in uneven #use forloop to iterate thru 1st list 
                 if num >= 5] #if statement if we want to add conditions to the return value 
print(even) 