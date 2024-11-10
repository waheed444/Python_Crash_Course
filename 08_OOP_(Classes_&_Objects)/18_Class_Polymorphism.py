# Polymorphism is often used in Class methods, where we can have multiple classes with the same method name.
# For example, say we have three classes: Car, Boat, and Plane, and they all have a method called move():

class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    
    def move(self):
         print(f"{self.brand} {self.model} is driving !")
class Boat:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    
    def move(self):
        print(f"{self.brand} {self.model} is sailing !")
        
class Plane:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    
    def move(self):
        print(f"{self.brand} {self.model} is flying !")
        
car1=Car("Toyota","Fortuner")
boat1=Boat("Ibiza","Turnning 20")
plane1=Plane("Boeing", "747")

for x in (car1,boat1,plane1):
    x.move()         # # Using polymorphism to call move method

        

    