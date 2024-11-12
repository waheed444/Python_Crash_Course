# 4. Fruit Ripeness Checker
# Determine if a fruit is ripe,overripe,unripe based on its color. 
# (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)
# Fruit Ripeness Checker

fruit = "Banana"
color = input("Enter the color of the banana to check ripeness (Green/Yellow/Brown): ").strip().capitalize()

if color == "Green":
    print(f"Your {fruit} is Unripe.")
    
elif color == "Yellow":
    print(f"Your {fruit} is Ripe.")
    
elif color == "Brown":
    print(f"Your {fruit} is Overripe.")
    
else:
    print("Please enter a valid color: Green, Yellow, or Brown.")

# .strip().capitalize() cleans up any extra spaces and capitalizes the input to handle case sensitivity.
