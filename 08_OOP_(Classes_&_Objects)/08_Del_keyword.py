# Del is used to delete the attributes of the class 
# Del is also used to delete the entire object 

class Student:
    def __init__(self,name):
        self.name=name
 
s1=Student("Waheed")
print(s1.name)       # Show the name "Waheed"
del(s1.name)         # Delete the attribute "Waheed"
print(s1.name)       # Error ! Because name "Waheed" has deleted