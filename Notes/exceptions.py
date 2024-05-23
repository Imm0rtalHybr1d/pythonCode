#example 

numbers = []
#_________________________ TRY...EXCEPT...ELSE_________________________
while True:
    #try block says try the following code thats indented beneath the try word 
    #and if their are any exceptions , rather exercute the code under the exept keyword
    try:
        x = int(input("Give an int: "))
    #if tryblock fails , then exercute the except     
    except (ValueError,NameError):
        print('Please enter an int not a str')
    #if try and except block doesnt exercute , then exercute this as last resort     
    else:
        print(x)   
        break
  

def get_input():
    #another example you could use is using the pass keyword , this catches the exception but does nothing with it 
    #it uses the pass keyword
    while True:
        #try block says try the following code thats indented beneath the try word 
        #and if their are any exceptions , rather exercute the code under the exept keyword
        try:
            return int(input('Enter a number: '))
        #if tryblock fails , then exercute the except     
        except (ValueError,NameError):            
        #here we catch the exception that we think could occur but instead of acting on it , we pass we do nothing    
            pass


#_________________________ TRY...EXCEPT...ELSE...FINALLY_________________________
#its always good practice to catch specific exceptions and then catch unknown exceptions
def get_list():
    while True:
        try:   
            uinput = int(input('Give numbers: '))            
           
        except NameError:
            print('please enter numbers only ')
            
        #you can also display what the actual exception is by using the following syntax 
        except ValueError as e:
            print(f'somthing went wrong heres the error : {e}')
            
        #the else keyword makes the program continue if there was no exceptions in our code
        #works as a success block             
        else:
            numbers.append(uinput)
            if len(numbers) == 5:
                break
            else:
                continue
        #you can use the finally keyword to exercute regardless of whether you caught any exceptions or not 
        finally:
            print('this code will always be exercuted because its in the finally block ')

#___________________RAISE_______________________________________

def check_age(age:int) -> bool:
    #you can explicitely raise an exception yourself 
    if age < 0 :
        raise ValueError('Not a valid age...')
    elif age <= 20:
        print('you are old enough')
        return True
    elif age <=21:
        print('You are not old enough')
        return False
    else:
        raise Exception('Blah')
check_age(2346) 


#______________________UKNOWN EXCEPTIONS_______________________

def catching() -> None:
    while True:
        user_input :int = '2tyy'
        
        try:
            number: float = float(user_input)
            print(f'you number is {number}')
        except Exception as e:# you can use the Exception keyword to catch unforseen errors
            print(f'Error: {e}')
            break
        else:
            print('No exceptions, this only prints when there are no exceptions')   
        finally:
            print('Finally - this prints always ') 
            break
catching()              