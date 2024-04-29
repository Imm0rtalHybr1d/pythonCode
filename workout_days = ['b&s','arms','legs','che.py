import datetime
today = datetime.date.today()

day_of_week = 'Tuesday'#today.strftime('%A')
print(day_of_week)

 #creating a list of exercises
exercises = ['Back & Shoulder','Arms','Legs','Chest']

#creating an empty list which is meant to hold the exercises that has been done
finished_exercise = [] 

#creating counter variable that counts how many times our loop has itterated
exit_value = 0 

#creating a list that stores the days of the week which we will use to match with the exercise
days_of_week = ['Monday','Tuesday','wednesday','friday'] 

#creating a loop that iterates though our exercises
for position, exercise in enumerate(exercises):
    finished_exercise.append(exercise)
    if days_of_week[position] == day_of_week:

        print("Today is ",days_of_week[position],'and we are doing' ,exercise)
        exit_value = exit_value + 1 
    break    
