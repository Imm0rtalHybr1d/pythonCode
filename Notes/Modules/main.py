#________________IMPORTING MODULES ________________
import Greetings  

# we can also import specific functions using the FROM keysword
from Greetings import greet

#we can also import a module and give it an Alias
import Greetings as G

if __name__ == '__main__':
    
    
    greet('Hano')

    #OR if you importing the entire module then you can use
    Greetings.greet('Bano')

    G.greet('Blahhhhh')