
# 8. Password Strength Checker
# Problem: Check if a password is "Weak", "Medium", or "Strong". 
# Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).

password = input("Enter your password to check the strength :")
pass_length = len(password)
if pass_length<6:
    print(f"Your password lenth is {pass_length}, Your password is Week")
elif 6<=pass_length<=10:
    print(f"Your password lenth is {pass_length}, Your password is Medium")
else:
     print(f"Your password lenth is {pass_length}, Your password is Strong")
    
