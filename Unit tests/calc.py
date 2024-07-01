
# SIMPLE CALCULATOR
def main()-> None:
    x:int = int(input('What is X? '))
    print(f'x squared is {square(x)}')
    
def square(x:int) -> int:
   return x*x     
 
if __name__ == "__main__":
    main()
 