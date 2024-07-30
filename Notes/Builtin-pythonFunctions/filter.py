numbers:list[int] = list(range(1,21))
print(f'Full list {numbers}')

#return bool if number can divide by 2 and have 0 remainder'''
def is_even(number:int) -> bool :
    return number % 2 == 0

#return true if number can divide by 2 and have a remainder
def uneven(number:int) -> bool :
    return number % 2 != 0

#Return an iterator yielding those items of iterable for which function(item) is true. 
# If function is None, return the items that are true.

#takes a function and applies it to an iterable and returns an iterable with only the result that is true 
even_number:filter = filter(is_even,numbers)
print(f'Even numbers: {list(even_number)}')

uneven_numbers:filter = filter(uneven,numbers)
print(f'Uneven numbers: {list(uneven_numbers)}')
'''
its not the most efficient to create a function just so that it can be used in the filter function
unless you are going to reuse that function , otherwise use a lambda function directly in the filter function
#can also use a list comprehension'''

even2_number:filter = filter(lambda n: n%2 == 0 ,numbers)
print(f'Even numbers: {list(even2_number)}')

people:list[str] = ['Ana','Kita','Mandy','Chris','Chevon']
long_names:filter = filter(lambda name: len(name) > 4,people)
print(f'Long Names: {list(long_names)}')




