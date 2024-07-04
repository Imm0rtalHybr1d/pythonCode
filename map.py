"""Map Function - map(function, iterable)
                - Returns an iterable where the function has been applied to every item in the provided iterable"""

numbers:list[int] =[1,2,3,4,5]
def double(number:int) -> int:
    return number*2

"""Using map function"""
doubled:map = map(double,numbers)

"""Using filter function"""
doubled:filter = filter(double,numbers)

"""Using a lambda """
doubled2:map = map(lambda n: n*2,numbers)

"""Can also use list comprehension"""
doubled3:list = [double(num) for num in numbers]

print(list(doubled))
print(list(doubled2))
print(doubled3)