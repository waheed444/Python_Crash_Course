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

# Example:

class Student:
    def __init__(self, name, marks):  # Constructor with name and marks parameters
        self.name = name              # Assign the student's name
        self.marks = marks            # Assign the student's marks
        
# Creating instances of Student with specific names and marks
student1 = Student("Waheed", 88)
student2 = Student("Ahmad", 92)

# Accessing and printing attributes of student1
print(f"Student Name: {student1.name}")
print(f"Marks: {student1.marks}")

# Accessing and printing attributes of student2
print(f"Student Name: {student2.name}")
print(f"Marks: {student2.marks}")
