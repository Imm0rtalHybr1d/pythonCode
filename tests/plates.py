plate_no = 'asdas'
max_char = 6
min_char = 2
counter = 0 


#takes a string and make sure its not more that 6 charachters 
def more_than_6(plate_no):
    if len(plate_no ) > max_char:
            print('Invalid')
    return 'Valid'   

#takes string and makes sure the first 2 letters are strings
def fist_two_is_str(plate_no):      
    
    #for each digit
    for char in plate_no: 
        #while counter is less than 2 , check if the first 2 characters are stringds
        try:
            char = int(char)
            return ('Invalid')

        except ValueError:
            
            counter+=1
            if counter >= 2:
                return 'Valid'   
            else:
                 return 'Invalid '
            
#first make sure user entered max of 6
#if it returns valid then we can check if the first 2 characters are letters
if more_than_6(plate_no) == 'Valid' :
    #call a function that checks the first 2 characters are letters in the string that user entered
    if  fist_two_is_str(plate_no) == 'Valid':
         print('Less than 6 and first 2 characters are') 