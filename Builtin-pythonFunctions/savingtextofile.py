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
             