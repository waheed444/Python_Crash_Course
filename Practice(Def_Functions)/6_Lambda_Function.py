
# 6. Lambda Function
# Problem: Create a lambda function to compute the cube of a number.

# Method -->1
def cal_cube(x):
    result = x **3
    return result

print(cal_cube(3))    

# Method -->2
cube = lambda x: x**3         # using lamda function
print(cube(2))



# Lambda functions in Python are anonymous, inline, and single-expression functions.
# They are used when you need a short, throwaway function without the overhead of defining a full def block


