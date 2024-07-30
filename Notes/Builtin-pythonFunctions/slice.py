#_____________________________SLICING__________________________________
numbers: list[int] = [1,2,3,4,5,6]
print(numbers[0:3]) #from 0 index to 3rd index
print(numbers[:3]) # everything up until 3rd index
print(numbers[3:]) #from 3 index 
print(numbers[-1])  #returns the last number in list

#we can also step over index
print(numbers[::2]) #prints everything in the list and steps by 2/prints every second letter 
print(numbers[::-1]) #steps backwords

#______________List Comprehention_____________________ 
sliced_list:list[int] = [num for num in numbers[0:5]]
print(sliced_list)

text:str = 'Hello'

#___Createing a SLICE Object that can be reused
first_three:slice = slice(0,3)

print(f'{text[first_three]}')

#creating a REVERSE SLICE OBJECT that can be resused 
reverser_slice: slice = slice(None,None,-1)
print(f'{text[reverser_slice]}')

