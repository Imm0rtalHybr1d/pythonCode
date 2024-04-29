def convert(time_str):
    # Split the time string into hours and minutes
    hours, minutes = map(int, time_str.split(':'))
    # Calculate the total time in hours
    total_hours = hours + (minutes / 60)
    return total_hours

def meal_time(time):
    # Define meal time ranges
    breakfast_start = 6.0
    breakfast_end = 11.0
    lunch_start = 11.0
    lunch_end = 14.0
    dinner_start = 17.0
    dinner_end = 20.0
    
    # Convert the time to hours
    time_hours = convert(time)
    
    # Check if it's breakfast time
    if breakfast_start <= time_hours <= breakfast_end:
        print("It's breakfast time!")
    # Check if it's lunch time
    elif lunch_start <= time_hours <= lunch_end:
        print("It's lunch time!")
    # Check if it's dinner time
    elif dinner_start <= time_hours <= dinner_end:
        print("It's dinner time!")

def main():
    time = input("Enter the time in 24-hour format (HH:MM): ")
    meal_time(time)

if __name__ == "__main__":
    main()







usertime = input()
hours,minutes = usertime.split(":")
newminutes = (minutes/60)

total_time = float(hours) + float(minutes)
print(total_time) 



#_________________________________________________
def main():

    #gets time from user and store it in the time variable
    time = '7:30'  #'input('Enter the time ')'''
    totaltime = convert(time)
   

    if 7.0 <= totaltime <= 8.0:  
        print("breakfast time")
    elif 12.00 <= totaltime <= 13.00:
        print('lunch time')
    elif 18.00 <= totaltime <= 19.00: 
        print("dinner time")
    else:
        return
        


def convert(time):
    #minutes will be dived by 100

    #splits hours and minutes into separate vaulues it and splts by the ':'
    hours, minutes = time.split(":")

    #both variables will be stored as float
    hours = float(hours) 
    minutes = float(minutes)

    #creates a variable that a  calls a function that passes 2 paramaters/variables
    #totaltime = convert(hoursfloat,minutesfloat)
    newminutes = float(minutes) / 60
    total = hours + newminutes
    return float(total )
   

if __name__ == "__main__":
    main()