
# 10. Recursive Function
# Problem: Create a recursive function to calculate the factorial of a number.


def factorial(n):        # Function Definition
    if n == 0:
        return 1 
    else:               # Recursive Case
        return n * factorial(n - 1)
    
print(factorial(5))     # Output: 120