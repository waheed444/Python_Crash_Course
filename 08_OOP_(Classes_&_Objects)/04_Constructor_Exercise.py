# Create student class that takes name & marks of 3 subjects as arguments in constructor.
# Then create a method to print the average.

class Student:                          # declar a class as Student
    def __init__(self,name,marks):      # define parametrized construction
        self.name=name
        self.marks=marks
    def avg(self):                      #def average function as avg()
        sum=0
        for value in self.marks:        #using for loop to get the average
            sum +=value
        print(self.name,"Average is :", sum/3)
            
s1=Student("Waheed",[77,85,60])        #store marks in the form of list    
s1.avg()                               #Print the Average of three marks
        