def main():

    #gets time from user and store it in the time variable
    time = '7:00'  #'input('Enter the time ')'''
    totaltime = convert(time)
   

    if 7.0 <= totaltime <= 8.0:  
        print("breakfast time...")
    elif 12.00 <= totaltime <= 13.00:
        print('lunch time...')
    elif 18.00 <= totaltime <= 19.00: 
        print("dinner time...")
    
        


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