#Print the elements of the following list using a loop:
num=[1, 4, 9, 16, 25, 36, 49, 64, 81,100]
for value in num:
    print(value)

#Search for a number x in this tuple using loop:
        
num=(1, 4, 9, 16, 25, 36, 49, 64, 81,100)
x=36
index=0
for val in num:
    if(val==x):
        print("found at the ",index)
    index+=1