class Car:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color
    
    @staticmethod
    def hello():
        print("Hello! This is a static method.")

# Creating an instance of the Car class
my_car = Car("Toyota", "Corolla", "2020")

# Accessing attributes
print(my_car.brand)
print(my_car.model)
print(my_car.color)

# Calling the static method
Car.hello()  
my_car.hello() # or you can also use my_car.hello()
