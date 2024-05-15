from unicodedata import digit


def main():
    printing(3)


def printing(digit):
    #for each of the digits in the range of 5
    for i in range(digit): # this loop is meant to iterate 5 times

        #for each position in the range of 5 digits please print # 
        for j in range(6): #this loop is meant to iterate 5 times
            print('poes', end="") #THE END KEYWORD IS IMPORTANT AS IT TELLS THE LOOP TO PRINT THE NEXT
        print()

main()        

