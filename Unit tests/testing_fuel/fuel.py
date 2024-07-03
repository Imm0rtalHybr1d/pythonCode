
def get_fraction(numb1:int,numb2:int) -> int|str:
    if numb1<numb2 and divid_by_0(numb1,numb2) == True:
        calc = numb1/numb2
        percentage:int = round(calc * 100)  
        return percentage
    elif numb1==numb2 and divid_by_0(numb1,numb2) == True:
        return f'F'
    else:
        return f'Enter a valid fraction'    
        
def split_convert(user_fraction:str) ->int:
    '''splits user's input so that the digits can be converter to int'''
    numb1,numb2 = user_fraction.split('/')
            
    if numb1.isdigit() and numb2.isdigit() :
        numb1 = int(numb1)
        numb2 = int(numb2)
        return numb1,numb2
    
def divid_by_0(numb1:int,numb2:int) -> bool|str:
    try:
        #if fraction not divided by 0 then its good, return true
        numb1/numb2 != ZeroDivisionError
        return True
    #else catch the ZeroDivisionError and return a message
    except ZeroDivisionError as e:
            return f'Cannot divide by Zero >>> {e}'
             

def main():
    #get user fraction
    users_fraction = input('Enter an expression: ') 
    try:
        '''split user str and converts it to a int'''
        numb1,numb2 = split_convert(users_fraction)
        
        '''use the converted ints to get the percetange'''
        percentage = get_fraction(numb1,numb2)
        
        #if percentage variable is a numeric digit then 
        if isinstance(percentage,int|float):
            if percentage <= 1:
                print('E')
            elif percentage >= 99:
                print('F')
            else:
                print(str(percentage)+'%')
        else:
            print(percentage)
            
    except (ValueError,TypeError,UnboundLocalError) as e:
        print(f'cannot use {users_fraction} as a fraction')
        print(f'Error: {e}')
    

if __name__ == '__main__':
    main()



