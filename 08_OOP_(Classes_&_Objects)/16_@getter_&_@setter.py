# # The getter and setter methods are used to access and modify private attributes of a class. 
# These methods allow you to control how attributes are accessed or modified, 
# ensuring encapsulation by restricting direct access to the data. In Python,
# we commonly use @property for defining getters and @property_name.setter for defining setters.
 
# What Are Getters and Setters?
# Getters: Methods that retrieve the value of an attribute.
# Setters: Methods that set or modify the value of an attribute, often with validation or checks


class Person:
    def __init__(self, name, age):
        self._name = name       # Private attribute
        self._age = age         # Private attribute

    @property
    def age(self):
        """Getter for the age attribute"""
        return self._age

    @age.setter
    def age(self, value):
        """Setter for the age attribute with validation"""
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value


person = Person("WAHEED AHMAD", 22)

# Accessing age using getter
print(person.age)  # Output: 25

# Setting age using setter
person.age = 30
print(person.age)  # Output: 30

# Attempting to set an invalid age
try:
    person.age = -5  # Raises ValueError: Age cannot be negative
except ValueError as e:
    print(e)
