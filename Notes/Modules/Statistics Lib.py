import random as r
import statistics

meen = statistics.mean([1,23,34,45,56,67,34,45,56,])
print(f'the mean is {round(meen,2)}')

test: list = [1,2,3,4,5,'blahhh','sdds','dsd']
#choses random choice
rand = r.choice(test)
print(rand)

#generates a random int with a give rand thats defined by a - start point and b- end point
rand_int = r.randint(a=-200,b=200)
print(rand_int)

#shuffles a list
r.shuffle(test)
print('Shuffled list:')
print(test)