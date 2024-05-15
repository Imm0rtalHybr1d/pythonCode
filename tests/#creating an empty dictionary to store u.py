input_counts = {}

while True:
    # Get user input
    try:
        user_input = input("Enter a value (or press control+c to exit): ")

    # Check if the user wants to quit
    

    # Update the input counts
        if user_input in input_counts:
        # If the input has been entered before, increment its count
            input_counts[user_input] += 1
        else:
        # If it's the first time, set its value to whateveer the value of count 
            input_counts[user_input] = 1
    except (KeyboardInterrupt,EOFError):
        print('')
        break
# Print the input counts

for value, count in input_counts.items():
    print(f"{count}: {value}")