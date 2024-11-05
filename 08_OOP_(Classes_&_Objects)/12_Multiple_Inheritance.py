# Multi-Level Inheritance Example
# In multi-level inheritance, a class inherits from a child class, creating a chain.

# Parent class
class Person:
    def __init__(self, name, age):
        self.name = name  
        self.age = age    

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

# Intermediate child class (inheriting from Person)
class Student(Person):
    def __init__(self, name, age, roll_no, year):
        super().__init__(name, age)
     
        self.roll_no = roll_no
        self.year = year

    def student_info(self):
        print(f"Roll No: {self.roll_no}, Batch Year: {self.year}")

# Further child class (inheriting from Student)
class GraduateStudent(Student):
    def __init__(self, name, age, roll_no, year, degree):
        super().__init__(name, age, roll_no, year)
        self.degree = degree                        # Specific to GraduateStudent

    def degree_info(self):
        print(f"Degree Program: {self.degree}")     # Specific to GraduateStudent

# Create an instance of GraduateStudent
grad_student = GraduateStudent("Waheed", 21, 93116, 2024, "Computer Science")

# Calling methods from Person, Student, and GraduateStudent classes
grad_student.introduce()       # Method from Person
grad_student.student_info()     # Method from Student
grad_student.degree_info()      # Method from GraduateStudent
