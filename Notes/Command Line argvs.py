import sys

try:
    #gets argument[1] from command line
    # print(f'Hello my name is {sys.argv[1]}') 
    
     #we can also ensure that user has entered the right amount of args using if len(arg[])    
    if len(sys.argv) < 2:
        print('Not enough arguments')
        sys.exit() #exits program 
        
except IndexError : #catches a possible exception
    print('Youre missing 1 argument')   

sys.argv.pop(0)         
for arg in sys.argv[::-1]:
    print("hello, my name is", arg)      
    