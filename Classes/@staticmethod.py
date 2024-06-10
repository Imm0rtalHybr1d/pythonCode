class Calculator:
    def __init__(self,version:int) -> None:
        self.version = version
    
    @staticmethod #a static method can be called without instantiating the class 
    def add( *numbers:float) -> float:
        return(sum(numbers))
    
    def get_version(self) -> int:
        return self.version

def main():
    # calc: Calculator = Calculator(version=1)
    result:float = Calculator.add(1.5,2.5,5.5,10.5)  
    #we can use the static method directly but using classname.methodname() --> Calculator.add()
    print(result)
    
def main():
    ...
if __name__ == "__main__":
    main()