# While loop - while something is true , keep doing whats inside the while loop 
#once statement is true then exit the loop 

#a variable is given a vaule of 1
i = 1

#the while loop statement says that while i is less than or equal to 3 then exercute the code within the while loop 
#if the statement is false, the while loop will not exercute
while i <= 3:
    i = i + 1
    print("the current value of the variable is",i)


#list - to contain multiple vaulues all in the same variable/place
#lists are represented by square brackets

#For loops - allows you to itterate over a block of code a fixed number of times 
#you can itterate over a range, string sequence list etc
#in the example below we using a for loop or iterate over a range from 0 - 4 
#this starts at 0 is the first vaulue and ends at 4 as the last vaulue within the range
for i in range(4):
    print ("the current value of the variable is",i) 

#you can also set where the loop counter starts within a range, see example below
for i in range(1,4):
    print ("the current value of the variable is",i) 

#you can also do a reverse loop - allowing the loop to itterate backwards
#you do this by enclosing the range function within the reverse function
for i in reversed(range(10)):
    print ("the current value of the variable is",i) 

#you can use the step parameter to count in n e.g to count in 2's we can use 2 as the step value 
#in this example we create a for loop that starts at 0 , goes to 10 and does it in 2's
for i in range(0,10,2):
    print ("the current value of the variable is",i) 

#you can also itterate over a string, see example below
card_No = '1234-5678-9-10'
for i in card_No:
    print(i)

#you can use certain keywords within forloops and whileloops such as :continue or break
#we use this if we want the loop to stop if a certain expression is true
#e.g  if we itterate thru a list and the i lands on a certain name within the list the we want to exit the loop
for i in range(15):
       #if the count/value of i reaches 9 , then we want the loop to skip over it
       if i == 9:          
           continue
       else:
           print('The current value of the variable is ',i)

#further explain using a list           
testlist = ['jack','hano', 'hiemie', 'carlos'] # creating a list that contains  names
for i in testlist:   #use the for loop to itterate thru the list with i representing the index/the position we are in the list
    if 'hano' in i or i=='hano':
        continue
    else:
        print(i)


#you can also create a loop where you dont actually want to use the variable in it , you simply want to iterate over a list/range/string
for _ in range(10):
      print('Hello world') 

#instead of using a forloop you can also use a multiply symbol 
print('Hello ' *3)      
#a for loop would be better suited if you not sure exactly how many times something should be printed

#if youre requesting user input that matches a certain expectation such as requesting strings only or requesting numbers only 
#then we use 

while True:
    n = int(input('Give me a positive integer number: '))
    if n < 0:
        continue #this means continue to stay in this loop
    else:
        print('Thanks, your number is ',n)
    break #will break you out of the most-recently begun loop

#another example
while True:
    uint = int(input('Give a number: '))  #ask for an input
    if uint > 0:  #if input more than zero , exit the loop
        break

for _ in range(uint):
    print('Hello')

#another example
def get_value():
    while True:
        userval = int(input('Give a number thats more than 0:'))
        if userval > 0 : 
            return userval
        
returned_val = get_value()        
print('He ',returned_val )
    
