import json
data: dict = {'name':'Bob',
              'age': 12,
              'job': None
              }
file_path:str = fr'C:\Users\01465307\Desktop\pythonCode\reading_writing JSON\data.json'

with open(file_path, 'a')as file:
    json.dump(data, file)
    print(f'finished dumping data intp data.json')