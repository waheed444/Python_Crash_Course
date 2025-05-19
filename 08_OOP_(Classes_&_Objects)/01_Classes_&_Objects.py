# Classes and objects in python 
# Class is the blue print of an object
# Example : if we make a student management system of a school using classes and objecs 
# we can make a class for "sudent" and make objects like their "makrs","roll no","subjects" etc 
class Student:              # class name start with class keyword
    
    name = "Waheed"         # name of every student is Waheed
    Roll_no = 2275 
                        
s1=Student()                # s1 is an object
print(s1.name)              # use object by " . " like .name
print(s1.Roll_no)

s2=Student()               # creates an instance (object) of the Car class.
print(s2.name)  
print(s2.Roll_no)         

class Car:                  # we declare a class as "car"
    brand = "BMW"          
    model = "2025"          #These are attributes of the class
    color = "Black"        

car=Car()                   #creates an instance (object) of the Car class.
print(f"Car Brand :{car.brand}")      
print(f"Car model :{car.model}")       #print the object using " . "  
print(f"Car Color :{car.color}")
