# Age Group Categorization:
# Classify a person's age group: 
# Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).

print(" Welcom to Age Group Categorization : ")
age = int(input("Enter you age here : "))

if age<13:    
    print(f'You age is {age}, you are Child')
    
elif age>=13 and age <=19:
    print(f'You age is {age}, you are Teenager')
    
elif age>=20 and age <=59:
    print(f'You age is {age}, you are Adult')
    
else:
    print("You are 60+, you are Senior")         
    
     
