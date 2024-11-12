# 6. Transportation Mode Selection
# Problem: Choose a mode of transportation based on the distance
# (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).


distance = int(input("Enter the distance in kilometers : "))

if distance<=3:
    print(f"You distance is {distance}.\n mode of transportation based on the distance is: \n---> Walk")
elif 3<distance<=15:
    
    print(f"You distance is {distance}.\n mode of transportation based on the distance is: \n---> Bike")
elif distance>15:
    
    print(f"You distance is {distance}.\n mode of transportation based on the distance is: \n---> Car")
else:
    print("Error Please enter a valid number here.")
