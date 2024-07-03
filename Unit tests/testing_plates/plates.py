
from curses.ascii import isalnum, isalpha, isdigit


#check:not longer than 6 digits and not less than 2
def check_max_length(plate:str) -> bool|str:
    max:int = 6
    if len(plate) <= max  :
        return True
    else:
        return f'{plate} has more than 6 characters'
    
#check:not longer than 6 digits and not less than 2
def check_min_length(plate:str) -> bool|str:
    min:int = 2
    if len(plate) >= min  :
        return True
    else:
        return f'{plate} has less than 2 characters'
    
        
# check:starts with 2 letters
def check_first_2(plate:str) -> bool|str:
    for letter in plate[0:2]:
        if isalpha(letter):
            continue
        else:
            return f'First 2 characters of {plate} need to be letters'
    return True

#check:if plate ends with letter
#if it ends with letter and charachter before that is a number then false
def ends_with_letter(plate:str) -> bool|str:
    last2:str=plate[-2:]
    try:
        if isalpha(last2[1]) and isdigit(last2[0]): # LAST
            return f'Numbers cannot be used in the middle of a plate >>> {plate}'
        else:
            return True
    except IndexError:
        return f'Plate cannot be a single digit'
    
#check: if first occurence of number is 0 then invalid
def first_num_0(plate:str) -> bool|str:
    #seprate digits using a forloop
    digits:list[int] = []
    for char in plate:
        if isdigit(char): 
            digits.append(int(char))
        else:
            continue    
    
    #check:if first num 0 
    try:
        if len(digits) >=1 and digits[0] == 0:
            return f'first number used cannot be 0 >>> {plate}'
        else:
            return True          
    except:
        return f'Plate cannot be a single digit'
    
def contains_punctuation(plate:str) -> bool|str:
    if plate.isalpha() or plate.isalnum() :
        return True
    else:
        return f'{plate} contains invalid characters , make sure its alphanumeric'
              
def main():
    plate = input('Plate: ')
    
    true_list:list[bool] = [check_max_length(plate),check_min_length(plate),check_first_2(plate),ends_with_letter(plate),first_num_0(plate)]  
    if all(true_list):        
        print('Valid')
    else:
        print('Invalid')    
    
 
if __name__ == "__main__":
    main()
     