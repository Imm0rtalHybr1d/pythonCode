def get_value():
    while True:
        userval = int(input('Give a number thats more than 0:'))
        if userval > 0 : 
            return userval
        
returned_val = get_value()        
print('Hello '*returned_val)