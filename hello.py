#creates a variable called userName and uses the input function to capture what the user types
userName = input ("Whats your name ?")

#prints space
print(" ")

#print 'hello' and the viarable userName which is captured using the input function in line 1
print("Hello " , userName)


"""the print function takes multiple functions
#print(*objects, sep=' ', end='\n', file=None, flush=False)
# using the sep end argument to specify waht the seperator is and that the next line shouldnt be printed on a new line as the default vaule for end is "\n" 
- which means goto a new line """
print ("Hello " ,userName,sep=". " ,end="" )



#using the + symbol to concatanate variables together
print(userName+userName+userName)

#using a string that contains ""
print('Hello "Friend"')
#can also use \ to get same result
print('Hello , \"Friend\" ')
#can also use a format string 
print(f'Hano {"tester"}')

#remove whitespace from string using .strip() method
userInput = input()
print('hello',userInput)

#creating a function removes whitespace using .strip() method
def stripWhiteSpc(userInput = input()):
    print( 'Hello,' ,userInput.strip())