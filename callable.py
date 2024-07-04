#_____Using Callable() to check if an object is can be called/used as a method

def func()->None:
    print('this function is callable')
    
def main():
    #use callable() function to check if another object is callable
    print(callable(func))
    func()
if __name__ == "__main__":
    main()
     