vowels = ['a','i','o','u','e'] 

#creating a list that stores the days of the week which we will use to match with the exercise
user_word = "whats i i my name"



#defining a function that creates a for loop
def loop_through(user_word):
     new_word = ""
    # this loop iterates through the list of extercises and then does checks 
    # each if statement is meant to take the current day and compare it to a predefined day 
    # if true then print the day of the week and which exercise the loop is currently on 
     for  letter in user_word:
        if letter in vowels:
            continue
        else:   
            new_word+= letter
            continue
     print(new_word)    
           

loop_through(user_word)        