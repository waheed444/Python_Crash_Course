# Python Tuples
# Tuples are ordered collection of data items. 
# They store multiple items in a single variable. 
# Tuple items are separated by commas and enclosed within round brackets (). 
# Tuples are unchangeable meaning we can not alter them after creation like lists

tuple=("ali","waheed","ahmad","umar")
print(tuple)                  
print(type(tuple))
print(len(tuple))
tuple1=(1,6,3,12,91,15,18,5,165,1,65,100)
print(tuple1)
color=("red","green","brown","black","yello")
print(color)
print(type(color))

#Tuple Indexes
#positive index
name=("ali","waheed","ahmad","rizwan","umar")
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
#negative Index
# The last item has index [-1]
# second last item has index [-2]
# third last item has index [-3] and so on.
name=("ali","waheed","ahmad","umar")
print(name[-1])
print(name[-2])

#check presence
#we can use conditional statements in tuples like lists
name=("ali","waheed","ahmad","umar")
if "ali" in name:
    print("ali is present")
else:
    print("ali is absent")


