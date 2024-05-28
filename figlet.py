from pyfiglet import Figlet
import random
import sys

figlet = Figlet()

#gets list of available fonts
avail_fonts = figlet.getFonts()

def random_font(user_input:str):
    #GETS random number using the length of the list
    number = random.randint(1,len(avail_fonts))

    #chooses random font
    avail_fonts[number]
    
    # sets the font to the random one 
    figlet.setFont(font=avail_fonts[number])

    #prints the text in FIGLET
    print(figlet.renderText(user_input))

def selected_font(user_input:str,user_font:str ):   
        figlet.setFont(font=sys.argv[2]) 
        #prints the text in FIGLET
        print(figlet.renderText(user_input))
        
def check_font(user_font:str) ->bool:
    if user_font in avail_fonts:
        return True
     
if len(sys.argv) == 1: #no args given
    user_input = input("Input: ")
    random_font(user_input)
     
if len(sys.argv) == 3 :
    
    if sys.argv[1] in ['-f', '--font']:
        if check_font(sys.argv[2]):
            #get input from user
            user_input = input('Input: ')
            selected_font(user_input=user_input,user_font=sys.argv[2])
        else:
            sys.exit('Invalid usage')    
    # elif sys.argv[1] == '--font':
    #     if check_font(sys.argv[2]):
    #         #get input from user
    #         user_input = input('Input: ')
    #         selected_font(user_input=user_input,user_font=sys.argv[2])
    else:
        sys.exit('Invalid usage')        
else:
    sys.exit('Invalid usage')   
