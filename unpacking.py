def demonstrate_multiple_assignment():
    """
    Demonstrates multiple assignment in Python.
    """
    a, b = [1, 2]
    print(f'{a=} {b=}')


def demonstrate_extended_unpacking():
    """
    Demonstrates extended unpacking in Python.
    a=first value, *b= second value up until except last value, c= last value
    """
    a, *b, c = 1, 2, 3, 4, 5, 6, 7, 8
    print(f'{a=} {b=} {c=}')


def extract_last_value(sequence):
    """
    Extracts the last value from a sequence and returns it.
    
    :param sequence: A sequence (e.g., string)
    :return: The last character of the sequence
    """
    *_, last = sequence
    return last


def add_numbers(a:int,b:int):
    """
    Adds two numbers together and prints the result.
    
    :param numbers: A dictionary containing two integers under keys 'a' and 'b'
    """
    print(f'{a+b=}')

def unpacking() -> None:
    """
    The function `unpacking` unpacks a list of numbers and a dictionary of parameters to pass them as
    arguments to the `print` function.
    """
    numbers: list[int] = [1,2,3,4,5]
    params:dict[str:str] = {'sep': '-','end':'.'}
    
    print(*numbers,**params)

def main():
    demonstrate_multiple_assignment()
    demonstrate_extended_unpacking()
    last_char = extract_last_value('abcedf')
    print(f'Last character: {last_char}')
    
    numbers:dict[str:int] = {'a': 5, 'b': 10}
    add_numbers(**numbers) #double ** indicated that it will be unpacking a dict, 
    #single * means its unpacking a list
    
    unpacking()
    
if __name__ == "__main__":
    main()