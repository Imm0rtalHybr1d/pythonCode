#creates a dictionnary that contains the fruit and the calaries 
Fruits = {
    "Apple": 130,
    "Avocado": 50,
    "Banana": 110,
    "Cantaloupe": 50,
    "Grapefruit": 60,
    "Grapes": 50,
    "Honeydew Melon": 50,
    "Kiwifruit": 90,
    "Lemon": 15,
    "Lime": 20,
    "Nectarine": 60,
    "Orange": 80,
    "Peach": 60,
    "Pear": 100,
    "Pineapple": 50,
    "Plums": 70,
    "Strawberries": 50,
    "Sweet Cherries": 100,
    "Tangerine": 50,
    "Watermelon": 80,
}


#gets user input and make sure its a string
#once we know its a string , the funtion returns whatever fruit the user typed 
def check_input():
    while True:
        try:
            user_input = input("Item: ").lower()   
            return user_input
        except ValueError:
            print('Please enter fruit names')
        
           
        
def check_calories(u_fruit):
    for fruit in Fruits:
        if fruit.lower() == u_fruit.lower():
            return print(f'Calories: {Fruits[fruit]}')
        else:
            continue    
def main():
   u_fruit = check_input()
   check_calories(u_fruit)

main()    