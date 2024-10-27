# __init__()  Function:
# In Python, the __init__ method is a special function called a constructor.
# It runs automatically when a new object is created from a class.
# This allows us to set up initial values for the object’s attributes when it’s created.
    
class Car:
    def __init__(self, brand, model, color):  # Constructor method with parameters
        self.brand = brand      # Assign the brand attribute to the given brand
        self.model = model      # Assign the model attribute to the given model
        self.color = color      # Assign the color attribute to the given color

# Creating an instance of Car with specific brand, model, and color
car1 = Car("BMW", "2025", "Black")

# Accessing and printing attributes of car1
print(car1.brand)
print(car1.model) 
print(car1.color)  


# Two Types of Consturctors:
# 1--> Default Constructor           e.g:  With no parameters
# 1--> Parameterized Constructor     e.g:  With some parameters  Like Car class
