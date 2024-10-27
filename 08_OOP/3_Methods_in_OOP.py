# Methods are functions that belong to objects.
# Define Student class
class Student:
        
    # Constructor to initialize name and marks
    def __init__(self, name, marks):
        self.name = name        # Set the student's name
        self.marks = marks      # Set the student's marks

    def welcome(self):           # Method to display a welcome message
        print("Hello Welcome Students!")  # Print welcome message

# Create a Student instance with name "Waheed" and marks 88
s1 = Student("Waheed", 88)
s1.welcome()                 # Call the welcome method

print(f"Student's Name: {s1.name}")    # Print the student's name and marks
print(f"Student's Marks: {s1.marks}")   
