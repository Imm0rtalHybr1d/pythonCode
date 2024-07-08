"""Zip Function - zip( iterable,iterable,*)
                - Returns an zip object where 2 or more lists have been 
                - Returns a list of grouped tuples
                - the length of the zipped object will always be that of the shortest list passed into it """
                
numbers: list[int] = [1,2,3,4]
letters: list[str] = ['a','b','c']
symbols: list[str] = ['!','@','#']

zipped:zip = zip(numbers, letters)
print(f'{zipped}')
print(list(zipped))

for n,l in zipped:
    print(f'{n}:{l}')
    
"""
If we zip up 2 lists that are of a diffrent size, by default the zipped list will be the length of the shortest list
but we can use strict mode which will raise an exception if the if youre trying to zip lists that are diffrent sizes
"""    
zipped2:zip = zip(symbols,numbers,strict=True)
print(list(zipped2))