# 5. Weather Activity Suggestion
# Problem: Suggest an activity based on the weather 
# (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman).

str="Weather"
str2 = input("Enter the weather to suggest acitivity (Sunny/Rainy/Snowy): ").strip().capitalize()

if str2 == "Sunny":
    print(f"Weather is {str2} outside.\nSuggestion:\nYou can Go for a walk.")
    
elif str2 == "Rainy":
    print(f"Weather is {str2} outside.\nSuggestion:\nYou can Read a book.")
    
elif str2 == "Snowy":
    print(f"Weather is {str2} outside.\nSuggestion:\nYou can Build a snowman.")
    
else:
    print("Please enter a valid weather: (Sunny/Rainy/Snowy).")

# .strip().capitalize() cleans up any extra spaces and capitalizes the input to handle case sensitivity.







