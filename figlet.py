from pyfiglet import Figlet
import random

figlet = Figlet()

#gets list of available fonts
avail_fonts = figlet.getFonts()

#GETS random number using the length of the list
number = random.randint(1,len(avail_fonts))

avail_fonts[number]

user_input = 'Blah'

# sets the font 
figlet.setFont(font=avail_fonts[number])

#prints the text in FIGLET
print(figlet.renderText(user_input))
