# @property decorator : 
# The @property decorator in Python allows you to define methods in a class that can be 
# accessed like attributes. This provides a clean way to define "read-only" properties or
# computed attributes withoutexposing them as public instance variables.
class Student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem 
        self.math=math 
        
    def cal_percentage(self):
        self.percentage=str((self.phy+self.chem+self.math) / 3)
        return str(self.percentage) + "%"
        
        
s1=Student(77,88,66)
print(s1.cal_percentage())


# Using @property Method 
class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"

# Create an instance of Student
s1 = Student(77, 88, 66)

# Access the percentage as an attribute
print(s1.percentage)
  