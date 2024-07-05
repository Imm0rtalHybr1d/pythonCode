from pyclbr import Function 

"""Lambda function = function written in 1 line using lambda keyword
                     accepts * amount of arguments but only has one expression
                     think of it as a shortcut
                     useful if you need it for a short period of time, like a throwaway"""
                     
# lambda paramater(s):expression
double:Function = lambda num: num*2 #<-- simple lambda function that multiplies a number by 2 
multiply:Function = lambda x,y:x*y

#simple example:
d_num:int = double(2)
print(d_num)

#example of use 
numbers:list[int] = list(range(1,10))
doubled_numbers:list[int] = map(lambda num: num * 2,numbers) #<-- use lambda fucntion in filter function 
test_list_comp:list[int] = [num*2 for num in numbers]
multiplied:list[int] = multiply(2,5)

print(list(doubled_numbers))
print(f'{multiplied}')
print(f'tested list comp {test_list_comp}')