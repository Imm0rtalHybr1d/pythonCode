from datetime import datetime

months : list[str] = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

#checks if user entered a valid month
def check_month(month) -> bool : 
    #if month is int and its less thatn 3 digits and falls within range 1-2 then its valid
    try:
        month == int(month) 
        if len(month) < 3 and 1<=int(month) <=12 :
            return True
        
    #else we know its a string , lets see if that string is part of our list
    except ValueError:               
            if month.capitalize() in months:
                return True

#check if user entered a valid day - it should be int and it should be between 1 and 31 and it should be < 3 characters 
def check_day(day) -> bool:
    try:
        day == int(day) 
        if len(day) < 3 and 1<=int(day) <=31 :
            return True
        else:
            return False
    except:
        return False    
            
def convert_str_date() ->str:      
    # Parse the date string
            date_object = datetime.strptime(user_input, "%B %d, %Y")

            # Format the date in desired format
            formatted_date = date_object.strftime("%m-%d-%Y")

            return formatted_date  # Output: 09-08-2024

            # month,day,year = user_input.split(sep=' ')
            # new_day = day.strip(',')

def check_month_str(month) -> bool:
     if month in months:
        return True    
     

while True:
    try:
        #user will always insert date as MM/DD/YYYY
        user_input = input('Enter a valid date: ')
        if ',' in user_input:
            month,day,year = user_input.split(sep=' ')
            new_day = day.strip(',')
        
            if check_day(new_day) == True and check_month_str(month) == True:           
                print(convert_str_date())
                break
            
            
            
        elif '/' in user_input: 
            month,day,year = user_input.split(sep='/')
            if check_day(day) and check_month(month) == True:
                print(year+'-'+month+'-'+day)  
                break
        #calls funtion that checks if the month is valid
        if check_month() == True:
          print(convert_str_date()) 

        # if check_day() == True:
        #     print(year+'-'+month+'-'+day)      

        # else:
        #     continue

    except ValueError as e:
        print(e)
    
    
    #     break
    # else:
    #     continue
    # #if user enteres a year with 4 digits , make sure its numbers 
    # if len(year) == 4 and int(year):
    #     print(year+'-'+month+'-'+day) 
    
 #if month is not a string(meaning its int) 
    #and the length of that int is less than 3 digits
    #and if that int falls within the range of 1 - 12 (essentially representing the months)         





#format that the date should be outputted YYYY-MM-DD
# print(year+'-'+month+'-'+day)