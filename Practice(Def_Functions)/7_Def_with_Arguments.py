
# 7. Function with Arugments
# Problem: Write a function that takes variable number of arguments and returns their sum.

def sum_all(*args):  
    print(args)          # Covered my arguments(values) in tuple 
    return sum(args)

print(sum_all(1,2,3,4))