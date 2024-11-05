# Inheritance :
# Inheritance is a fundamental concept in Object-Oriented Programming (OOP) that 
# allows a class (called a "child class" or "subclass") to inherit attributes and 
# methods from another class (called a "parent class" or "superclass"). 
# This helps promote code reuse and establishes a relationship between different classes.


# Define the parent class "Person" :
class Person:
    def __init__(self, name, age):
        self.name = name  
        self.age = age   

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

# Child class (single-level inheritance)
class Student(Person):
    def __init__(self, name, age, roll_no, year):
        super().__init__(name, age)

        self.roll_no = roll_no
        self.year = year
        
    def student_info(self):
        print(f"Roll No: {self.roll_no}, Batch Year: {self.year}")

# Create an instance of Student
student = Student("Waheed", 21, 93116, 2024)

# Calling methods from both Parent and Child classes
student.introduce()              
student.student_info()          
# Access only child class attributes
print(student.name)          
print(student.age)           


# Control Flow of Output:
# -->  Always execute child class frist 
# -->   Then execute parent class 