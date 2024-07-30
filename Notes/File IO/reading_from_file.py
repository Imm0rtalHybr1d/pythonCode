# This code snippet is opening a file named `names.txt` in read mode located at
# `c:/Users/01465307/Desktop/pythonCode/File IO/`. It then reads all the lines from the file and
# stores them in a list called `filelines`. Finally, it prints out all the lines in the file using the
# `print(*filelines)` statement. The `with` statement is used to ensure that the file is properly
# closed after reading, even if an error occurs during the reading process.

with open(f'c:/Users/01465307/Desktop/pythonCode/File IO/names.txt', 'r') as file:
    filelines:list[str] = file.readlines()
    print(*filelines)
    
print(f'')   

#could also print the lines like this
with open(f'c:/Users/01465307/Desktop/pythonCode/File IO/names.txt', 'r') as file:
    filelines:list[str] = file.readlines()
    
    #sorting the lines 
    sorted_filenames: sorted = sorted(filelines)
    for line in sorted_filenames:
        print(line,end="")  
          
    print(f'')      
    print('another example')
    print(f'')
    
    #another example of sorting
    for line in sorted(filelines):
        print(f'{line}',end="")    
        
