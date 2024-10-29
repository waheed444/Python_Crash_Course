# 2. Movie Ticket Pricing
# Problem: Movie tickets are priced based on age:
# $12 for adults (18 and over), $8 for children( ,17 and less1). Everyone free who is 60+
age = int(input("Enter you age here:"))
if age >=18 and age<=60:
    print("You are adult, You Movie ticket price = 12 $")
elif age <18:
    print("You are child, You movie ticket price = 8 $")
else:
    print("You are 60+, You are free")
    