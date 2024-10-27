#WAP to find the Grade students based on marks

marks=int(input("Enter the marks of the students:"))
print("Your marks out of 100 is ",marks)
if(marks>100):
    print("Error!\nPlease enter marks bw 1 to 100")
elif(marks>=90):
    print("grade=A")
elif(marks>=80):
    print("grade=B")
elif(marks>=70):
    print("grade=C")
elif(marks>60):
    print("grade=D")
else:
    print("Invalid")