#  Leap Year Checker
# Problem: Determine if a year is a leap year. 
# (Leap years are divisible by 4, but not by 100 unless also divisible by 400).

year = int(input("Enter year to check leap or not : "))
if year%400==0 or year%4==0 and year%100!=0:
    print(f"{year} is leap year")
else:
    print(f"{year} is not leap year")
    
    
# Leap Year Rules:

# A year is a leap year if:
# It is divisible by 400 (e.g., 2000, 2400), OR
# It is divisible by 4 but not by 100 (e.g., 2024, 2028).
# Condition Explanation:

# (year % 400 == 0): This checks if the year is divisible by 400.
# If a year satisfies this condition, it’s always a leap year (e.g., 2000).
# (year % 4 == 0 and year % 100 != 0): This checks if the year is divisible by 4 but not by 100.
# This rule catches most leap years, but it excludes years like 1900 and 2100, which are divisible by 4 and 100 but not by 400.
# Logical Operators:

# The or operator connects these two checks, so if either condition is true, the year is considered a leap year.
# Example Execution for the Year 2023
# Step 1: (year % 400 == 0):
# 2023 % 400 is not 0, so this condition is False.
# Step 2: (year % 4 == 0 and year % 100 != 0):
# 2023 % 4 is not 0, so this condition is also False.
# Since both conditions are False, the else block runs, printing 2023 is NOT a leap year.