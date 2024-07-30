import json


# This code snippet is reading a JSON file located at the specified file path
# (`C:\Users\01465307\Desktop\pythonCode\data.json`). 
# It uses the `json.load()` function to load the
# contents of the file into a Python dictionary named `data`. The line `data: dict = json.load(file)`
# specifies that the variable `data` is of type `dict` (dictionary) and assigns the loaded JSON data
# to it. Finally, it prints out the contents of the `data` dictionary using `print(f'{data}')`.
file_path: str = fr'C:\Users\01465307\Desktop\pythonCode\reading_writing JSON\data.json'

with open(file_path) as file:    
  data: dict = json.load(file) #loads JSON file into a dictionary 
  print(f'{data}')
    
    
    
#you can also load string data thats in the form of JSON data into a dict using json.loads()    
my_json: str = """{
  "name": "Bano",
  "age": 262,
  "Friends":["Msdario", "Luigsdi"],
  "Other info": null
}"""

my_dict: dict = json.loads(my_json) #we use .loads() to load the string object
print(f'{my_dict}')