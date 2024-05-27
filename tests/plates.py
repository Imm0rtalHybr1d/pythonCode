import string

plate_no = 'asdas'
max_char = 6
min_char = 2
counter = 0 


#takes a string and make sure its not more that 6 charachters 
def more_than_2(plate_no):
    if 2 < len(plate_no ) <= 6 :
        return 'Valid'
    else:
        return 'Invalid'   

#takes string and makes sure the first 2 letters are strings
def fist_two_is_str(plate_no) -> bool:      
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


def two_true(plate_no:str) -> str:
    # counter =0
    # for char in plate_no[:2]:
    #     if char.isalpha() and counter<=2:
    #         counter+=1
    #     return 'Invalid'
    if plate_no[:2].isalpha():
        return 'Valid'
    else:
        return 'Invalid'       
    
    
    
    
            
#first make sure user entered max of 6
#if it returns valid then we can check if the first 2 characters are letters
if more_than_2(plate_no) and two_true(plate_no) == 'Valid' :
    ...
