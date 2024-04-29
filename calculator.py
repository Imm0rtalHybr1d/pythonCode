#can nest functions - we nesting the int() which converts string to an int , within the print function 
print(int(5) * int(2))

#using float - decimal point
x = float(1.222222) + float(2.545455)
print(x)

#using the round() function to round off decimal numbers 
round(x,2)
print(x)

# round (number [,ndigits])  - square brackets indicate optional input by user 
#here we round off to nearest 2 digits after decimal - this is represented by the 2 after the comma
xx=round(1000.55555,2)
print(f"{xx:,}")


z = float(10/33)
print (f'{z}' , + 'this is before using the round()')
z = round(10/33)
print (z)

z = float(0.555)
print (z )


float(round(f"{1000.2222:.2f}"))
print ()
