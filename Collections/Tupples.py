#tupples , very similar to a list , main diffrence is that data in tupple cannot be changed/minpulated as in a list
#its immutable i.e you cannot change it 
#tuple is faster than lists 
#its stored on 1 block of memory compared to lists which are 2 blocks of memory
#what the usecase ? 
#for quick fetching data , function returns
#if you know the data will never change then use a tupple, else use a list
Coordiantes : tuple[float]= (2.3, 34.4, 5.4)
version_number: tuple[float,str] = (2.133, 'Alpha') #here we creat a tupple and specify the data that is stored at each index

 
#can also be be used with conditionals
t1: tuple[int] = (1, 2, 3) 
t2: tuple[int] = (2, 3, 4)

if t1 >= t2:
    print ('True')
else:
    print('False')

#if you wanna set something you could use a tupple
Software_version :tuple[float] = (1.23)  #in this example we declare that the software version is 1.23 using a tupple , this will not change throught our program