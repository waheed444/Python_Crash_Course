# 4. Reverse a String
# Problem: Reverse a string using a loop.
  
# To reverse a string using a loop, we’ll iterate through the string from the end to
# the beginning and construct a new string with the characters in reverse order.


original_string = "Hello, World!"

reversed_string = ""     # Initialize an empty string to hold the reversed result

for char in original_string:   # Loop through the original string backwards
  # Add each character to the beginning of the reversed_string
    reversed_string = char + reversed_string    

print("Original string:", original_string)
print("Reversed string:", reversed_string)
