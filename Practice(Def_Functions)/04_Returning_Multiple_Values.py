# 4. Function Returning Multiple Values
# Problem: Create a function that returns both the area and circumference of a circle given its radius.


# Function to find area of a circle

def area(num):
    result1=3.14*num*num
    print(f"Area of circle is : {result1}")
    return result1


# Function to find circumference of a circle
def circumference(num):
    result2 = 2*3.14*num
    print(f"Circumference of circle is : {result2}")
    return result2

# We can take input(radius) from the user :
# radius = float(input("Enter radius here : "))
area(5)
circumference(5)

# Method # 2 --> We can also use one function to find both area+circumference
def circle(num):
    area = 3.14*num*num
    circumference = 2*3.14*num
    print(f"Area : {area} \nCircumference : {circumference}")
    return area,circumference

# We can take input(radius) from the user :
# radius = float(input("Enter radius here : "))
circle(5)