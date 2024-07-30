from typing import TextIO

file_path: str = fr'C:\Users\01465307\Desktop\pythonCode\testing.txt'


file: TextIO = open(file_path, 'r')
text: str = file.read()
text3: str = file.read(2) # you can specify how many characters you want to read by passing in a value 

print(f'{text, text3}')
file.close()

