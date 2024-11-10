# 3. Multiplication Table Printer
# Problem: Print the multiplication table for a given number up to 10,
# but skip the fifth iteration.

num = int(input("Enter any number to printer the table :"))
for i in range(1,11):       
    if i==5:
        continue                # skip 5th iteration 
    print(f'{num} x {i} = {num*i}')