#function is used to perform same specific task multiple times in a same program
#function must have  any arguments and parameters
  
def addition(a,b):    #function defination
    sum=(a+b)         #body of the function(arrguments/parameters)
    print("The sum of a and b is :",sum)
def subtraction (a,b):
    sub=(a-b)
    print("The sub of a and b is :",sub)
def multiplication(a,b):
    mul=(a*b)
    print("The mul of a and b is :",mul)
def division(a,b):
    div=("The div of a and b is :",a/b)
    print(div)    
# Function  is defined  before(outside) the actuall program>
a=10
b=20
addition(a,b)             #calling the function
subtraction(a,b)
multiplication(a,b)
division(a,b)