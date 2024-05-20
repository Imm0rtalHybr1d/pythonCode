import datetime
from datetime import datetime
import time

def show_time():
    #creating a variable called now ,of type : datetime and set it to datetime.now() which gets the current date and time 
    time: datetime = datetime.now()
    
    
    # we print the now variable and use the % syntax to format it as hours, minutes, seconds 
    print(f'Time: {time:%H:%M:%S}') 
    
      
def show_date ()-> str:      
    #date: datetime = datetime.date.date()
    today = datetime.today()
    print(f'Date: {today:%d/%m/%Y }')
    
    
show_time()       
time.sleep(5)
show_date()