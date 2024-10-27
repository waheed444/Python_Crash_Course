name=("ali","waheed","Hamza","Hussnain")
#convert tuple into list
temp=list(name)   #temp keyword is used to convert tuple into the list
#add ahmad into the list
temp.append("Ahamd")     
#specify the place (index)
temp.pop(3)   #pop is used to add something in the specific index in the list(conveted to tuple)
#reconvert list into tuple
name=tuple(temp)
#print tuple
print(name)


#tuple 1
countries = ("Pakistan", "Afghanistan", "Bangladesh", "SriLanka")
#tuple 2
countries2 = ("Vietnam", "India", "China")
# new tuple = tuple 1 + tuple 2
southEastAsia = countries + countries2
print(southEastAsia)

# count method()
num=(1,3,1,30,1,10,9,13,135,130,13,1)
print(num.count(1))

#index() method
num1=(1,3,1,3,1,10,9,13,135,130,13,1)
#first occurence of 3 is on the 1 index 
print(num1.index(3))

