
#list is used to store the multiple type of data within the sqaure bracket[]

num=[4,"Waheeed",16,74,8,95,20,21,2,3]   
print(num)       #print the all elements of the list 
print(len(num))  #print lenth of all elements in the list
print(type(num)) #print the type of the list

#list can contains integers,numbers,alphabets,strings,multiple data types

name=["ali","waheed","hassan","ahmad"]
#index  0      1        2        3
print(name)
print(name[0])   #print the 0 index 
print(name[1])   #print the 1 index 
print(name[2])   #print the 2 index 
print(name[3])   #print the 3 index 

#print(name[4])   #python  shows the error because 4 index  not  found

#we can also conditional conditions  in list 
if 16 in num:
    print("Yes")
else:
    print("No")
if "waheed" in name:
    print("Yes")
else:
    print("No")       
















