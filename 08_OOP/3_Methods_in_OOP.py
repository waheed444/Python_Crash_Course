# Methods are functions that belong to objects.
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def welcome(self):
        print("")
s1=Student("Waheed",88)
print(f"Student's Name :{s1.name}")   
print(f"Student's Marks :{s1.marks}")   