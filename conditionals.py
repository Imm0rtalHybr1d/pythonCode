def greet():
    greet = ("hello world")
    if greet == "hellsssddo world":     #opening up using the if statement
        return ("sd") 
    
#creating a basic If statement within a function
def testingIf(input):
    if 'hello' in input:
        print('hello there')
    else:
        print('bye')

testingIf(input())

#creating another if statement and using return values
def guessAns():
    userans = int(input('Give a number'))
    return userans

def main():
    userAns = guessAns()
    print (userAns)
    
#conditional statement checking if the greet method returns a certain text, if so then print certain text
if greet() == "hellsssddo world":     #opening up using the if statement
    print("sd") 
elif greet() == "hellssdo world":     #using elif to do further checks 
    print("Mo")
elif greet() == "sd world":
     print(greet(), '!!!!!!')   
else:                              #using else to exercute if none of the above if/elif statements are true
    print("Nothing Matches")


#defining a method that returns hello world 
def greet():
    return("hello world")
   
#conditional statement checking if the greet method returns a certain text, if so then print certain text
if greet() == "hellsssddo world":     #opening up using the if statement
    print("sd") 
elif greet() == "hellssdo world":     #using elif to do further checks 
    print("Mo")
elif greet() == "sd world":
     print(greet(), '!!!!!!')   
else:                              #using else to exercute if none of the above if/elif statements are true
    print("Nothing Matches")



if greet() == "hello world" or   greet() == "hellsssddo world":  #opening up using the if statement
    print(greet())   
#using conditional statement but using the OR keyword to see if its true to something else 
if greet() == "hello world" or  greet() == "hellsssddo world":  #opening up using the if statement
    print(greet())     

greetVal = 'Hello world'    
if greetVal == "hello world" or  greetVal == "hellsssddo world":  #opening up using the if statement
    print(greet())   




#using conditional statement but using the AND keyword to see if its true to something else 
x = int(input('Give a number '))
y = int(input('give another number '))
if x==2 and y<=3:
    print('both numbers are less than 4')
else:
      print('nah fam , that ain it')  




#more on conditional if statements
#compareing scores using if staements 
score = int(input('Score: '))

if score >= 90 and score <= 100:
    print('Grade: A ')
elif score >= 80 and score<90:
    print('Grade: B')      
elif score >= 70 and score <80:
    print('Grade is C')    
elif score >= 60 and score <70:
    print('Grade: C')       
elif score >= 50 and score <60:
    print('Grade: D')      
else:
    print('Grade: F')    

#can reduce this code and nest the AND statement like this 
if 90 <= score <=100:
    print('Grade: A ')
elif 80 <= score <=90:
    print('Grade: B')         

#using the modus operator to check if user entered an even number
#  modus divides a number into another number and returns the remainder
# if  x modus 2 has no remainder then print even,else print odd
x = int(input('Whats X ? '))    
if x % 2 == 0:
    print('Even')
else:
    print('Odd! , the remainder is 1 = ')   
    print('The remainder of ',x ,' /2 is ',  x % 2, sep='')  



##further using boolean values and conditional statements to get a certain output
#if the is_even() function is true , then print even , if its false print odd
def main2():
    xx = int(input('Whats X ? ')) 
    if is_even(xx):
        print('Even')
    else:
        print('Odd! , the remainder is 1')   
        print('The remainder of ',x ,' /2 is ',  x % 2, sep='')  


def is_even(x):       
    if x % 2 == 0:
        return True
    else:
        return False  
    #COULD CONDENSE THE ABOVE CODE AND USE one single line - but i prefer to have it spread out for better readabilityt
        #return True if x % 2 == 0 else False

    #could even simplify it futher
    return x % 2 == 0  
main2()


