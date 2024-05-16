#returns nothing - None Means nothing , can be used as a placeholder 
no_value: None = None

users:dict = {1:'hano', 2:'Bano'}

possible_user : str | None = users.get(3) #tries to fetch the value of key 3 
print(possible_user)