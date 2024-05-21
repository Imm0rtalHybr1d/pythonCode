#some functions in python can include * and /

#______________USING /_________________________
def func(var_a:str, / ,var_b:str) -> None:
    print(var_a)
    print(var_b)
    
    # this indicates that any arguments before the / cannot be passed as a keyword arguemnt
    # anything before the / must be passed as a positional argument
    
def func2(vara:int,/,varb:int) -> None:
    print(vara,varb)    
    
func2(vara=23,varb=23)
#this would output an error as we are trying to pass vara as a keyword argument
#the / explicitly means that anything before it must be passed as a positional argument




#______________USING *_________________________
#when defining a function that has * , this means that every argument has to be passed by its keyword
#the * explicitly means that any argument after it must be passed as a keyword argument
def meth(char_a:str ,*,char_b:str,char_c:str ) -> None:
    print(char_a,char_b,char_c)
    
meth('sdsdsd',char_b='sdsdd',char_c='sgh234sddsd')   