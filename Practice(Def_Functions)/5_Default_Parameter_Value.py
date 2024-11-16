# 5. Default Parameter Value
# Problem: Write a function that greets a user. If no name is provided, it should greet with a default name.

def greet(name):         # With no parameters
    print(f"Hello {name} !")
    return greet

greet("WAHEED")

def greet(name="User"):    # with default parameter "User"
    print(f"Hello {name} !")
    return greet

greet()    
greet("WAHEED")