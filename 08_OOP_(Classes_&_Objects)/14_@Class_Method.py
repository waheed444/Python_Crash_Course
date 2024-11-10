# In Python, the classmethod() function is used to define a method that is bound to the class
# and not the instance of the class. This means that it can be called on the class
# itself rather than on instances of the class. Class methods are useful when
# you need to work with the class itself rather than any particular instance of it.

# Example # 01
class Person:
    
    name = "anonymous"  
    def ChangeName(self, name):
        self.name = name  # `self.name` creates or updates the instance attribute `name`
        
person = Person()            # Creates an instance of Person
person.ChangeName("Waheed")   # Changes the instance attribute `name` to "Waheed"
print(person.name)            # Output: "Waheed" (instance attribute)
print(Person.name)            # Output: "anonymous" (class attribute)


# Example # 02
class Person:
    
    name = "anonymous" 
    def ChangeName(self, name):
        Person.name = name  # Changing the class attribute directly using the class name
        
person = Person()            # Creates an instance of Person
person.ChangeName("Waheed")   # Changes the class attribute `name` to "Waheed"
print(person.name)            # Output: "Waheed" (class attribute now changed for all instances)
print(Person.name)            # Output: "Waheed" (class attribute updated)


# Example # 03
class Person:
    
    name = "anonymous" 
    def ChangeName(self, name):
      self.__class__.name = name  # `self.__class__` refers to the class (Person), updating its attribute `name`
        
person = Person()            # Creates an instance of Person
person.ChangeName("Waheed")   # Changes the class attribute `name` to "Waheed"
print(person.name)            # Output: "Waheed" (class attribute now changed for all instances)
print(Person.name)            # Output: "Waheed" (class attribute updated)
