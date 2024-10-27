# WAP to check if a number entered by the user is postive or negative.

num = int(input("Enter the numbers :"))
print("You entered number  is  :",num)
if num<0:
    print("You number  is negative")
elif num==0:
    print("You number is zero")
else:
    print("You number is positive")