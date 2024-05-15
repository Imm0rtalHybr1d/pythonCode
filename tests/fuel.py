def get_fraction() -> float:
    while True:
        try:
            #get user fractions
            users_fraction = input('Enter an expression: ')
            numb1,numb2 = users_fraction.split('/')
            numb1 = int(numb1)
            numb2 = int(numb2)

            if  divid_by_0(numb1,numb2) == False:
                continue
            elif numb1>numb2:
                continue


            calc = numb1/numb2 
            percentage = round(calc * 100)
            return percentage
        except ValueError:
            print('Please use numbers in your fraction')  
            continue
        except ZeroDivisionError:
            print('You cannoit divide by 0')      
            continue
        

def divid_by_0(numb1,numb2: int) -> bool: 
    try:
        numb1/numb2 == ZeroDivisionError
    except ZeroDivisionError:
            return False

        


# #this give us the fraction based on the user's input 
# calc = numb1/numb2 
# percentage = round(calc * 100,0)
# # print(round(calc * 100),'%')
percentage =get_fraction()
if percentage <= 1:
    print('E')
elif percentage >= 99:
    print('F')      
else:
    print(str(percentage)+'%')