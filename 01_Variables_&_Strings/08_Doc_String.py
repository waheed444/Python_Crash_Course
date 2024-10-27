#Python docstrings are the string literals that appear right after
#  the definition of a function,method, class, or module.

def square(n):
    
    '''Takes in a number n, returns the square of n'''
    print(n**2)
square(5)
print(square.__doc__)

#doc string is just like the commments but not actually comments.
#it can be  executed  unlike the comments by ''.__doc__''
#it help to print write the discription of the program and execute it on demand.


