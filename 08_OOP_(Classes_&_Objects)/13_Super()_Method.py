# Super() Funtion is used to access the method of the parent's class

class Car: 
    def __init__(self,type):
        self.type=type
        
    @staticmethod
    def start():
        print("Car started...")
    
    @staticmethod
    def stop():
        print("Car stoped...")
        
class Toyota(Car):
    def __init__(self,name,type):
        self.name=name
        super().__init__(type)

my_car=Toyota("Fortuner","Electric")
print(my_car.type)        
        