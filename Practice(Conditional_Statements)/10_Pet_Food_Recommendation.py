# 10. Pet Food Recommendation
# Problem: Recommend a type of pet food based on the pet's species and age.
# (e.g., Dog: <=2 years - Puppy food, Cat: >5 years - Senior cat food).

pet = input("Enter pet your (Dog or Cat):")
pet_age = int(input("Enter pet's age: "))

if pet_age<=2:
    print("Your pet's food : Puppy Food")
    
else:
    print("Your Pet's food : Senior Cat Food")
    