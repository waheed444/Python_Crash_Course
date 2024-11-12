# 3. Grade Calculator
# Problem: Assign a letter grade based on a student's score: 
# A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).

grade = int(input("Enter you score here (0 to 100) :"))

if 90<=grade<=100:
    print(f"You score is {grade},Your grade is A")
    
elif 80<=grade<=89:
    print(f"You score is {grade},Your grade is B")
    
elif 70<=grade<=79:
    print(f"You score is {grade},Your grade is C")
    
elif 60<=grade<=69:
    print(f"You score is {grade},Your grade is D")
    
elif grade<60:
    print(f"You score is {grade},Your grade is F")
    
else:
    print("Error! Please enter score (0 to 100)")