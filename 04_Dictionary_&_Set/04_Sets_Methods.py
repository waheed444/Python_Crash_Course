#Sets in python more or less work in the same way as sets in mathematics.
#We can perform operations like union and intersection on the sets just like in mathematics.

set1 = {1,2,34,5,6,56,5,3,4,3,43,55,46,45,43,43}

set2 = {33,76,2,43,43,3,43,4,6,54,64,67,56,7,67,4,53,}

#collect all element of both sets (print once repeated elements)

set3 = set1.union(set2)   

print(set3)

#print common elements of both sets

set3 = set1.intersection(set2)      

print(set3)

#note: We cannot store dictionary and list in set