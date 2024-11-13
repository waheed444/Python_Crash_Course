# 1. Basic Function Syntax
# Problem: Write a function to calculate and return the square of a number.

# Method no 01:
# def sqr(a):
#     result=a**2
#     print(f"Square of {a} is {result}")
# a=2
# sqr(a)

def sqr(a):
    result=a*a
    print(f"Square of {a} is :{result}")
    return result

(sqr(2))