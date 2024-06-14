import sys
import time

def welcome_message() -> None:
    print('Welcome to the Groceries List')
    print('Enter: ')
    print('------------------------')
    print('1 - To add an item ')
    print('2 - To remove an item ')
    print('3 - To list all items ')
    print('0 - To add an item ')
    print('------------------------')
    
def add_item(item:str,groceries:list[str]) -> None:
    groceries.append(item)
    print(f'{item} added!')
    
def remove_item(item:str,groceries:list[str]) -> None:
    try:
        groceries.remove(item)
        print(f'{item} has been removed')
    except ValueError:
        print(f'No "{item}" found in: {groceries} ')
        
def display(groceries :list[str]) -> None:
    print('____LIST____')
    
    for i, item in enumerate(groceries,1):
        print(f'{i}: {item.capitalize()}')
    print('_'*10)        
    
def is_an_option(text:str) -> bool:
    return text in ['1','2','3','4','0']

def update_item(old_item:str,new_item:str, groceries:list[str]) -> None:
    updated_list:list[str] = []
    
    for i,item in enumerate(groceries):
        if item == old_item:
            groceries[i] = new_item
                   
    print(groceries)        
            
        
def main() -> None:
    groceries : list[str] = []
    welcome_message()
    
    while True:
        user_input:str = input('Choose: ')
        
        if not is_an_option(user_input):
            print('Please pick a valid option...')
            continue
        
        if user_input == '1':
            new_item:str = input('What item would you like to add? >> ').lower()   
            if new_item != '' and len(new_item) > 1:         
                add_item(new_item,groceries)
            else:
                print(f'Cannot add "{new_item}"')    
            
        elif user_input == '2':
            rem_item:str = input('What item would you like to add? >> ').lower()            
            remove_item(rem_item, groceries)
            
        elif user_input == '3':
               display(groceries) 
               
        elif user_input == '4':
            old_item = input('Name of the item youd like to update ')

            new_item = input('Enter the new value ')
            update_item(old_item,new_item,groceries)
                      
        elif user_input == '0':
            print('Exiting...')
            time.sleep(3)
            sys.exit()       
            
if __name__ == '__main__':
    main()        