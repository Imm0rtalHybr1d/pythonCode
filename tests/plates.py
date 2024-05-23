import string

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
def fist_two_is_str(plate_no) -> True:      
    counter :int = 0
    alphabet :str = string.ascii_letters
    string.digits
    
    for char in plate_no:
        while counter < 2:
            if char in alphabet:
                counter+=1
                continue
            else:
                return 'Invalid'    
        return 'Valid'
    
    
    
    
    
            
#first make sure user entered max of 6
#if it returns valid then we can check if the first 2 characters are letters
if more_than_6(plate_no) and fist_two_is_str(plate_no) == 'Valid' :
    ...
