# This code essentially writes the
# contents of `name1` and `name2` to a file named `names.txt`, with each string on a new line.
name1 = 'test 1: writing to a file'
name2 = 'test 2: writing to a second line in a file'
# write mode (`'w'`), which means that if the file does not exist, it will be created, and if it does
# exist, its contents will be overwritten.
file = open(f'c:/Users/01465307/Desktop/pythonCode/File IO/names.txt', 'w')
file.write(f'{name1}\n')
file.write(f'{name2}\n')
file.close()

#another example using 'a' to append
file = open(f'c:/Users/01465307/Desktop/pythonCode/File IO/names.txt', 'a')
file.write(f'{name1}\n')
file.write(f'{name2}\n')
file.close()

#another example without having to call the close method
with open(f'c:/Users/01465307/Desktop/names.txt', 'a') as file:
       file.write('this line was written using the with open syntax')


"""Working Example"""       
test:list[str] = ['nlah', 'blah']

def save_weather_to_file(data:list, filename:str):
    # Open the file in write mode
    with open(filename, 'w') as file:
        # Write weather data to the file
        for element in data:
            file.write(f"{element}\n")
                                                               
def main():
    save_weather_to_file(test,'test.txt')
 
if __name__ == "__main__":
    main()
                    