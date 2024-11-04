# Abstraction:
# Hiding the implementation(uneccessary) details of a class and 
# only showing the neccessary features to the user.

class Car:   
    def __init__(self):        # Initial state of each component is set to False 
        self.key=False 
        self.fuel=False
        self.speed=False
        self.brake=False
        self.clutch=False
        
    def car_start(self):        # Turn on necessary components to start the ca
        self.key=True
        self.fuel=True
        self.speed=True
        self.brake=True
        self.clutch=True
        print("Car is stated........")
   
    def stop_car(self):              # Turn off components when stopping the car
        self.key = False
        self.fuel = False
        self.speed = False
        self.brake = False
        self.clutch = False
        print("Car is stopped.")
        
my_car=Car()
my_car.car_start()

