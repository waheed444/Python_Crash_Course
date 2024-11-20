# Python has a set of built-in math functions, including an extensive math module,
# that allows you to perform mathematical tasks on numbers.


# The min() and max() functions can be used to find the lowest or highest value in an iterable:

x = min(5, 10, 25)
y = max(5, 10, 25)

print("Minium :",x)
print("Maximum :",y)

# The abs() function returns the absolute (positive) value of the specified number:

x = abs(-7.25) 
print(x)    

# The pow(x, y) function returns the value of x to the power of y (xy).

x = pow(4, 3)
print(x)    # Return the value of 4 to the power of 3 (same as 4 * 4 * 4):


import math 
print(math.sqrt(625))    # returns the square root of a number

x = math.ceil(1.4)      # rounds a number upwards to its nearest integer
y = math.floor(1.4)     # rounds a number downwards to its nearest integer

print(x) # returns 2
print(y) # returns 1

x = math.pi          # The math.pi constant, returns the value of PI (3.14...):
print(x)

