# 8. Prime Number Checker
# Problem: Check if a number is prime.

number = int(input("Enter any number here: "))
is_prime = f"Yes, {number} is Prime"

if number > 1:
    for i in range(2, number):    # Prime number starts from "2"
        if (number % i) == 0:     # divisible by ourself = Prime
            is_prime = f"No, {number} is not Prime"
            break
        
print(is_prime)