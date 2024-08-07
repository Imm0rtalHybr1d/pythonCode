# 'The code snippet is creating a list of integers called `num_list` with the values `[1234, 424, 54, 5784, 784, 1, 2, 254, 817, 454, 78451, 7]`.
# 'It then sorts this list in ascending order using the `sorted()` function and assigns the sorted result to a new list called `sorted_list`.
# 'Finally, it prints the sorted list.
num_list:list[int] = [1234,424,54,5784,784,1,2,254,817,454,78451,7]
sorted_list:list[int] = sorted(num_list)
print(sorted_list)

"""if using strings, it sorts in alphabetical order by its ascii value"""
name_list:list[str] = ['Ana','Kita','Mandy','Chris','Shevon']
sorted_name_list:list[str] = sorted(name_list)
print(sorted_name_list)

"""Can also sort in backwards, using -> reverse keyword"""
num_list2:list[int] = [12,24,54,5784,784,54,87,454,78451,7]
sorted_list2:list[int] = sorted(num_list,reverse=True)
print(f'Reversed sroted list using reverse=True >>> {sorted_list2}')

"""We can specify how we want to sort using -> 'key='"""
name_list2:list[str] = ['Ana','Kita','Mandy','Chris','Chevon']
sorted_name_list2:list[str] = sorted(name_list,key=lambda name: len(name ))
print(sorted_name_list2)
print(f'_____')
print(f'_____')

class Animal:
    def __init__(self,name:str,weight:float) -> None:
        self.name = name
        self.weight = weight
        
    def __repr__(self) -> str:
        return f'{self.name} = {self.weight}kg'        
    
cat:Animal = Animal('Tommy', 3.5)    
dog:Animal = Animal('Lola',10)
dog2:Animal = Animal('Jack',5)
dog3:Animal = Animal('Nayla',7.5)

sorted_animals:list[Animal] = sorted([cat,dog,dog2,dog3],key=lambda animal: animal.weight)
print(list(sorted_animals))