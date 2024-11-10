# 7. Validate Input
# Problem: Keep asking the user for input until they enter a number between 1 and 10.

while True:
    number=int(input("Enter any number between 1 to 10:"))
    if 1<=number<=10:
        print('Thanks! You entered : ', number)
        break
    else:
        print("Error! Please enter number between 1 to 10")