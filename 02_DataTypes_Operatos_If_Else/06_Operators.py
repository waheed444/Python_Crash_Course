# # There are many types of operators in the python used to perform specific taks
# Operators must have two value that values are called as operands 
a=5
b=3
# Arithmatic Operators
print(a+b)     #addition
print(a-b)     #subtraction
print(a*b)     #multiplication
print(a/b)     #division
print(a%b)     #modolus (gives reminder)
print(a**b)    #Exponentional (5*5*5)
print(a//b)    #Floor Divison (rounds the result to the nearst whole number)
# Relational/Compaerision Operators

print(a<b)    #5<3 False
print(a>b)    #5>3 True
print(a==b)   #5=3 False
print(a!=b)   #5 not equal to 3 True
print(a<=b)   #5<=3 false
print(a>=b)   #5>=3 True

# Assignment Operators
num=10
print(num)    #10
num +=10     
print(num)   #10+10=20
num -=10
print(num)   #20-10=10
num *=10
print(num)   #10*10=100
num /=10
print(num)    #100/10=10
num %=10
print(num)    #10/0=0
num **=10     
print(num)     #0*0=0

#Logical Operator
#not Operator
a=50
b=30
print(not False)
print(not (a>b))    #not(!) make true to false and false to true
#and Opeartor
val1=True
val2=False
print("AND Operator is :",val1 and val2)        #if both is true then true otherwise false
#Or Operator
print("OR Operator is :",val1 or val2)          #if both is false then false otherwise true
