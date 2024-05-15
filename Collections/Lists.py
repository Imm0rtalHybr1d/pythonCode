#simple syntax to create a list 
#using square brackets to index into the list and get the second value of the list 
#lists are zero indexed , meaning its first value is position/index 0
#using the square brackets allows us to go inside a listand specify the value we want using an index

students: list[str] = ['carlos','hano','nueeb','hiemie']

my_list: list = [1, True, [1,2,3,4]] #- lists can hold any datatype as an element 
my_list.append('another entry') #using append() function to add elements to the list

print(students[1])

for student in students:
    print(student)


#another way of doing this  function returns a number of items in an container (cnstainers can be
#the len() lists, arrays,dictionaries)
for i in range(len(students)):
    print(students[i])
    
