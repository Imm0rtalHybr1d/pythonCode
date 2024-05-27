from pyfiglet import Figlet
import random

figlet = Figlet()

#gets list of available fonts
avail_fonts = figlet.getFonts()

#stores a random font in this var
rand_font = random.choice(avail_fonts)

user_input = 'Blah'

# sets the font 
figlet.setFont(font=rand_font)

#prints the text in FIGLET
print(figlet.renderText(user_input))
