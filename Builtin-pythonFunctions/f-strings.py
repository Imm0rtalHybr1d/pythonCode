# The code snippet is defining a function `format_strings` that formats a big number and prints it
   # in two different ways.
def format_ints(big_number:float)->None:
   
  # The code `print(f'{big_number:,}')` is using f-string formatting to print the `big_number`
  # variable with a comma as a thousands separator. This means that the number will be formatted with
  # commas and underscores separating every three digits for better readability.
   print(f'{big_number:,}')
   print(f'{big_number:_}')

def format_fraction(fraction:float) -> None:
    """
    The function `format_fraction` takes a float value representing a fraction and prints it with two
    decimal places."""
# The code `print(f'{fraction:.2f}')` is using f-string formatting to print the `fraction` variable
# with exactly two decimal places. This means that the float value will be displayed with two digits
# after the decimal point.
    print(f'{fraction:.2f}')
    
   # The code `print(f'{fraction:,.2f}')` is using f-string formatting to print the `fraction`
   # variable as a float with exactly two decimal places. Additionally, the comma (`,`) inside the
   # curly braces is used as a thousands separator. This means that the float value will be displayed
   # with commas separating every three digits for better readability, and it will have exactly two
   # digits after the decimal point.
    print(f'{fraction:,.2f}')

def format_percent(percent:float) -> None:
    """
    The function `format_percent` takes a float value representing a percentage and prints it with two
    decimal places and a percentage sign.
    """
    print(f'{percent:.2%}')
    
def format_strings(var:str) -> None:
    """
    The function `format_strings` takes a string variable and prints it with a specific formatting.
    
    :param var: The `var` parameter in the `format_strings` function is a string type variable
    :type var: str
    """
    print(f'{var:10}: Hi') #use 10 spaces
    print(f'{var:<10}: Bye') #left alligned
    print(f'{var:>10}: Cry')#right alligned
    print(f'{var:^10}: Lie')#center alligned
    print(f'{var:_^10}')# use _ instead of spaces
 
def format_raw_string(path:str) -> None:
    print(path)    
    
        
def main():
    big_number:float = 123456789
    format_ints(big_number)
    
    fraction:float = 1234.5678
    format_fraction(fraction)
    
    percent:float = 0.5
    format_percent(percent) 
    
    var:str = 'Bob'
    format_strings(var)
    
    # The code snippet is defining a string variable `user` with the value `'01465307'`. Then, it
    # constructs a file path string `path` using an f-string with the `user` variable interpolated
    # within the path. The `fr` prefix before the string indicates that it is a raw string, which
    # means backslashes are treated as literal characters and not as escape characters.
    user:str = '01465307'
    path:str = fr'\Users\{user}\Desktop\pythonCode'
    format_raw_string(path)
 
if __name__ == "__main__":
    main()
 

