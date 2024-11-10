# What about classes with child classes with the same name? Can we use polymorphism there?
# Yes. If we use the example above and make a parent class called Vehicle, and make Car, Boat,
# Plane child classes of Vehicle, the child classes inherits the Vehicle methods, but can override them:

class Vehical:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    
    def move(self):
         print("This vehical is moving !")


class Car(Vehical):
    def move(self):
         print(f"{self.brand} {self.model} is driving !")\
             
class Boat(Vehical):
    def move(self):
        print(f"{self.brand} {self.model} is sailing !")
        
class Plane(Vehical):
    def move(self):
        print(f"{self.brand} {self.model} is flying !")
        
car1=Car("Toyota","Fortuner")
boat1=Boat("Ibiza","Turnning 20")
plane1=Plane("Boeing", "747")

for x in (car1,boat1,plane1):
    x.move()       # # Using polymorphism to call move method
