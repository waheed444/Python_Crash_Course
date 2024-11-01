# 1. Counting Positive Numbers
# Problem: Given a list of numbers, count how many are positive.
# numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

# Given list of numbers
numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

# Count the positive numbers using list comprehension
positive_count = sum(1 for num in numbers if num > 0)

# Output the result
print("Number of positive numbers:", positive_count)
