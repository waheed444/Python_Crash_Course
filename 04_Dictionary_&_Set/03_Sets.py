#  Sets are unordered collection of data items.
#  They store multiple items in a single variable.
#  Set items are separated by commas and enclosed within curly brackets {}
#  The order is always different for each run(not specified/unordered)

set(key, value, coded_value)={1,3,4,56,6,6,5,4,55,24,55,4,}
print(set)

#use for loop to print the values in the set
for value in set:
    print(value)

# empty set
waheed={}                        #This is empty dictionary not empty set  
print(type(waheed))

ali=set()
print(type(ali))                  #This is empty set 

info = {"name", 19, False, 5.9, 19}
print(info)