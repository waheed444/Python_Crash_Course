# 2. Sum of Even Numbers
# Problem: Calculate the sum of even numbers up to a given number n.

# Let given number is 10 
# Input: Define the value of n
n = 10
even_sum = 0
for num in range(1, n + 1):  # Loop through all numbers from 1 to n
    if num % 2 == 0:         # Check if the number is even
        even_sum += num
        
print("Sum of even numbers up to", n, "is:", even_sum)
