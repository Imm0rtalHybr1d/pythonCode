#creating a main method/function and in the main method , we call another method call HellO()
def main():
    Hello()


#here we define the hello() method and what it does
def Hello(x='World'):
     print('hello',x)

#we call the main() method whos function is to call the Hello() method
main()    


#creating a functions called Hello() , which takes a string variable called x but x also has a default vaulue incase x isnt assigned a value
def Hello2(x='World'):
    print('hello',x)

#calling the hello2() funtion with an argument
X = input('Whats your name?')
Hello2(X)

#calling the hello() without parsing an argument
Hello2()

#defining a function called guessAns() that stores user input in usersans variable, whenever this function is called , it returns a value back  another if statement and using return values
def guessAns():
    userans = int(input('Give a number '))
    return userans

def main():
    userAns = guessAns()

    if userAns == 50:
        print ('Correct Answer !')
    else:
        print ('Incorrect Answer !')


#defining a function that checks if a number that user entered is even
def is_even(x):       
    if x % 2 == 0:
        print('Even')
    else:
        print('Odd! , the remainder is 1')   
        print('The remainder of ',x ,' /2 is ',  x % 2, sep='')  

xx = int(input('Whats X ? ')) 
is_even(xx)