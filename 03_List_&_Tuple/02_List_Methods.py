
# There are many methods(operations) used in list 
# list.sort()
num=[1,6,3,41,9,400,49,61,18,56,14,500]
# This method sorts the list in ascending order. The original list is updated
num.sort()      
print(num)  

colors = ["voilet", "indigo", "blue", "green"]   #(Short list from a to z form)
colors.sort()
print(colors)
#reverse()
# What if you want to print the list in descending order?
# We must give reverse=True as a parameter in the sort method.
list=[1,6,3,41,9,400,49,61,18,56,14,]
# This method sorts the list in decending order. The original list is updated
list.sort(reverse=True)      
print(list)  

# count()
# Returns the count of the number of items with the given value. 
num1=[1,6,3,41,9,1,400,49,61,56,1,1,14,1]
print(num1.count(1))

# append():
# This method add items to the end of the existing list.

# Example:

colors = ["voilet", "indigo", "blue", "green"]
colors.append("Red")   
print(colors)

# insert():
# This method inserts an item at the given index. 
# User has to specify index and the item to be inserted within the insert() method.

# Example:
colors = ["voilet", "indigo", "blue"]
#           [0]        [1]      [2]

colors.insert(1, "green")   #inserts item at index 1
# updated list: colors = ["voilet", "green", "indigo", "blue"]
#       indexs              [0]       [1]       [2]      [3]

print(colors)

# extend():
# This method adds an entire list or any other collection datatype 
# (set, tuple, dictionary) to the existing list.

# Example 1:

#add a list to a list
colors = ["voilet", "indigo", "blue"]
rainbow = ["green", "yellow", "orange", "red"]
colors.extend(rainbow)
print(colors)