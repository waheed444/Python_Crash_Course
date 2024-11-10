# 9. List Uniqueness Checker
# Problem: Check if all elements in a list are unique.
# If a duplicate is found, exit the loop and print the duplicate.
# items = ["apple", "banana", "orange", "apple", "mango"]

list = ["apple", "banana", "orange", "apple", "mango"]
unique_item = set()   # # Initialize an empty set to track seen items
for item in list:
    if item in unique_item:  # Loop through each item in the list
        print("Duplicate : ",item)   
        break    # Exit the loop as soon as we find a duplicate
    else:         
        unique_item.add(item)  # If not a duplicate, add it to the set
else:
    # If loop completes without breaking, all items are unique
    print("All items are unique.")