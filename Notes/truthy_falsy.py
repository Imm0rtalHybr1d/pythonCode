users:dict[int:str] = {1:'hano',2:'bano'}

#__________________TRUTHY_____________________
#we can check if something is true by evaluating if has data in it
#if users dict has data in it , it returns true, allowing the if condition to be satisfied
if users:
    for k, v in users.items():
        print(f'{v}')
else:
    print(f'no data found')        