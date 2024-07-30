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

def zipper(list1:list[int],list2:list[str],list3:list[str]) -> None:
    """
    The function `zipper` takes three lists of different types, zips them together element-wise, and
    prints the zipped result.
    
    :param list1: A list of integers:type list1: list[int]    
    :param list2: A list of integers:type list2: list[str]    
    :param list3: The `list3` parameter in the `zipper` function is a list of strings. It will be zipped
    together with `list1` (a list of integers) and `list2` (a list of strings) to create a new zipped
    list containing elements from all three lists
    :type list3: list[str]
    """
    zipped3: zip = zip(list1,list2,list3)
    print(list(zipped3))
    
def main():   

    zipper(numbers,letters,symbols)

 
if __name__ == "__main__":
    main()
     