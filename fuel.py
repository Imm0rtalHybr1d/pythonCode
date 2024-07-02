from curses.ascii import isalpha, isdigit



def get_fraction(users_fraction:str) -> int:
    '''splits user's input so that the digits can be converter to int'''
    numb1,numb2 = users_fraction.split('/')
            
    if numb1.isdigit() and numb2.isdigit() :
        numb1 = int(numb1)
        numb2 = int(numb2)
        if numb1<numb2 and divid_by_0(numb1,numb2) == False:
            calc = numb1/numb2
            percentage:int = round(calc * 100)  
            return percentage
        else:
            return f'{numb1} > {numb2}'    

def divid_by_0(numb1:int,numb2:int) -> bool:
    try:
        numb1/numb2 == ZeroDivisionError
    except ZeroDivisionError:
            return False

def main():
    #get user fractions
    users_fraction = input('Enter an expression: ') 
    percentage = get_fraction(users_fraction)

    if percentage <= 1:
        print('E')
    elif percentage >= 99:
        print('F')
    else:
        print(str(percentage)+'%')


if __name__ == '__main__':
    main()

percentage =get_fraction()

