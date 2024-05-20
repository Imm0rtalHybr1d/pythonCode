import datetime

#getting todays date and storing it in the today variable


day_of_week = today.strftime('%A')
#print(day_of_week)

 #creating a list of exercises
exercises = ['Back & Shoulders','Arms','Legs','Chest']

#creating an empty list which is meant to hold the exercises that has been done
finished_exercise = [] 


#creating a list that stores the days of the week which we will use to match with the exercise
days_of_week = ['Monday','Tuesday','Wednesday','Friday'] 


#defining a function that creates a for loop
def loop_through():
    # this loop iterates through the list of extercises and then does checks 
    # each if statement is meant to take the current day and compare it to a predefined day 
    # if true then print the day of the week and which exercise the loop is currently on 
    for position, exercise in enumerate(exercises):
        finished_exercise.append(exercise)
        #creating a loop that iterates though our exercises
        if day_of_week == 'Monday':
            print('Today is ',day_of_week, 'and we are doing', exercises[position] )
        elif day_of_week == 'Tuesday':
            print('Today is ',day_of_week, 'and we are doing', exercises[position] )
        elif day_of_week == 'Wednesday':
            print('Today is ',day_of_week, 'and we are doing', exercises[position] )
        elif day_of_week == 'Friday':
            print('Today is ',day_of_week, 'and we are doing', exercises[position] )
        else:
            print("we've iterated thru all our exercises")
        break

loop_through()


