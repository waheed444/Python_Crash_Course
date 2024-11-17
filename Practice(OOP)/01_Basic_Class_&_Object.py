#  Basic Class and Object
# Problem: Create a Car class with attributes like brand and model. Then create an instance of this class.
class Car:
    def __init__(self, brand,model):
      self.brand = brand
      self.model = model
    

my_car=Car("Toyota","2020")
print("Brand : ",my_car.brand)
print("Model :",my_car.model)

my_new_car=Car("BMW", "2025")
print("Brand : ",my_new_car.brand)
print("Model :",my_new_car.model)