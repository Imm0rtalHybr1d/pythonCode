#____________TO TEST calc.py functionality
from calc import square

def test_square() :

#___________1)USING assert() for ERROR CHECKING ___________ 
    try:
        assert square(2) == 4    
        assert square(3) == 93   
    except AssertionError as e: #Raises AssertionError if the assertion is not true
        print(f'{e}')  
    
    # another way to use it which includes a specified message
    assert square(3) == 93,'square root of 3 is not 93'   
    
def main():
    test_square()

if __name__ == "__main__":
    main()
             