#simple syntax to create a list 
students = ['carlos','hano','nueeb','hiemie']

my_list: list = [1, True, [1,2,3,4]] #- lists can hold any datatype as an element 

#using square brackets to index into the list and get the second value of the list 
#lists are zero indexed , meaning its first value is position/index 0
#using the square brackets allows us to go inside a listand specify the value we want using an index
print(students[1])

for each_student in students:
    print(each_student)


#another way of doing this 
#the len() function returns a number of items in an container (cnstainers can be lists, arrays,dictionaries)
for i in range(len(students)):
    print(students[i])
    
