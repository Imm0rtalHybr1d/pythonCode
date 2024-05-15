
#main funtion which stores user input
def main():
    camelCase = input("enter a word in camel case: ") #this will be user input

    #creates a new variable that stores wahtever value the check_user_input function does
    #pass in users input as a paramater
    final_camel_case = check_user_input(camelCase)
    print('snake_case version:',final_camel_case)


#creating a while loop that forces user to enter a string in camelCase
def check_user_input(user_input):
#while loop takes first letter of the user input which is a str and checks if its capitalized, 
#if it is , the loop will ask user to enter proper camelCase word
    while user_input[0].capitalize():
        user_input = input("enter a word in camel case, please note the first letter always starts with a lowercase letter ")
        continue
    else:
        #Final_Snake_Case = print(iterate(cameCase))
        return iterate(user_input)


#define a funtion that
def iterate(user_input):

    snake_case=""
    for letter in user_input:

        if letter == letter.capitalize():
            snake_case = snake_case+"_"

        snake_case = snake_case+letter.lower()
    return snake_case
main()