# The word "polymorphism" means "many forms", and in programming it refers to as 
# methods/functions/operators with the same name that can be executed on many objects or classes.

# Simple Example Addition with various methods
print(2+1)                   # Add two numbers
print("Waheed" + "Ahmad")    # Add two strings(Concatenate) 
print([1,2,3]+[4,5,6])        # Add two lists


# len() to find the length of characters
x = "Hello World!"
print(len(x))            # For strings len() returns the number of characters:

mylist = [1,3,5,7,9]
print(len(mylist))     # For Lists len() returns the number of items in the Lists:

mytuple = ("apple", "banana", "cherry") 
print(len(mytuple))  # For tuples len() returns the number of items in the tuple:

mydict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(len(mydict))   # returns the number of key/value pairs in the dictionary:
