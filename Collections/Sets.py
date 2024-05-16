#similar to lists
#no gaurenteed order, cannot contain duplicates
#the data is stored random 
#cannot refer to anything specific because sets are random 
elements: set = {99, True,'bob'} #so 99 can be at index 2 , it will be random everytime the script runs


elements.add('JAMES') #ADD ELEMENTS
elements.remove(True) #REMOVE ELEMENTS
elements.pop() #REMOVES RANDOM ELEMENT FROM SET
elements.clear()#CLEARS THE SET

#FORZEN SET__________________
#Immutable and Unordered also memory effecient like tupple
#once created , you cannot change the data inside
things: frozenset = (elements)