# Single-Level Inheritance Example
# In single-level inheritance, a child class directly inherits from a single parent class:

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

# Another Example
class Car:

    @staticmethod
    def get_start():
        print("Car is started...")

    @staticmethod
    def get_stop():
        print("Car is stoped...")
    
class Toyota(Car):
    def __init__(self,brand,color,price):
        self.brand=brand
        self.color=color
        self.price=price
        
        
my_car=Toyota("Toyota","Black",2022)
print(f"Car Brand : {my_car.brand}" )
print(f"Car Brand : {my_car.color}" )
print(f"Car Brand : {my_car.price}" )
    
print(my_car.get_start())
print(my_car.get_stop())
    
