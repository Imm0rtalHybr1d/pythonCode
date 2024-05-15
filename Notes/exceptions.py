#example 

numbers = []

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
  
#another example you could use is using the pass keyword , this catches the exception but does nothing with it 
#it uses the pass keyword
def get_input():
    while True:
        #try block says try the following code thats indented beneath the try word 
        #and if their are any exceptions , rather exercute the code under the exept keyword
        try:
            return int(input('Enter a number: '))
        #if tryblock fails , then exercute the except     
        except (ValueError,NameError):            
        #here we catch the exception that we think could occur but instead of acting on it , we pass we do nothing    
            pass



#its always good practice to catch specific exceptions and then catch unknown exceptions
def get_list():
    while True:
        try:   
            uinput = int(input('Give numbers: '))
            
        #you can also display what the actual exception is by using the following syntax    
        except NameError:
            print('please enter numbers only ')
        except ValueError as e:
            print(f'somthing went wrong heres the error : {e}')

        #the else keyword makes the program continue if there was no exceptions in our code             
        else:
            numbers.append(uinput)
            if len(numbers) == 5:
                break
            else:
                continue
        #you can use the finally keyword to exercute regardless of whether you caught any exceptions or not 
        print('this code will always be exercuted because its in the finally block ')

def main():
    get_list()
    for number in numbers:
        print(number)
    get_input()

main()    
get_input()