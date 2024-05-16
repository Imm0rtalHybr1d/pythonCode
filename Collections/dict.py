#dictionaries allow you to associate one value with another 
#dicts use Keys : value pairs
#below is the basic example of creating a dictionary

students = {
    "Hermoine": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}
#can print a spicific key by using the key as the index
print (students["Hermoine"]) #this will output 'Gryffindor
students['Harry'] = 'Slytherin' #can change a spicific value by using the key as the index

#STORING DICTS IN DICTS
weather: dict = {'time': '12:00',
                 'weather':{'Morning':'Rain',
                            'Evening':'More rain'}   
                }






#creating an empty dict
finished = {}
#another example
Workout = {
    "Monday" : "Legs",
    "Tuesday" : "Chest",
    "Wednesday" : "Back & Shoulders",
    "Friday" : "Second Legs",
    "Sunday": "Arms",
}

for k,v in Workout.items():
    print(k,v,sep=' ')


#we can also use a for loop to iterate through our dict
#using a for loop to iterate over a dictionary , by defaukt it iterates over the keys
#essentially saying for each key in this dictionary , please print that key
for exercise in Workout:
    #this simple prints our the key
    print (exercise )

    #here we print the vaulue by using the key as the index
    #for comparison the key is the word and vaulue is the definition
    print(Workout[exercise]) #print the value based on what the key is

    #testing the .update() funtion of dictionaries , to simply update/add an entry to our dictionary
    newentry = exercise,Workout[exercise]
    finished.update({newentry})
print(finished)
    

#if we want to print out a specific exercise we have to enter the key that is associated with the value
print (Workout["Monday"])   

  #____________________________________________________________________________________________________________________________________________________________________________


#creating a list of dictionaries 
testing =[
    {  "Exercise":"Legs", "Day":"Monday", "Max_Weight":"63kg"  },
    { "Exercise":"Chest", "Day":"Tuesday", "Max_Weight":"63kg"  },
    { "Exercise":"Back & Shoulders", "Day":"Wednesday", "Max_Weight":"38kg"  },
    { "Exercise":"Second legs", "Day":"Friday", "Max_Weight":None  }
]

#using a for loop to iterate thru the each key value pair FOR each dictionary 
for test in testing:
    print(test["Exercise"], test["Day"], test["Max_Weight"])
    