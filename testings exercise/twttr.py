vowels = ['a','A','i','I','o','O','u','U','e','E']

#creating a list that stores the days of the week which we will use to match with the exercise
# user_word = input('Input: ')

#defining a function that creates a for loop

    
def loop_through(user_word):
    new_word = ""
    # this loop iterates through each letter within a word and then does checks
    for  letter in user_word:
        if letter in vowels:
            continue
        else:
            new_word+= letter
            continue
    return(new_word)


 


