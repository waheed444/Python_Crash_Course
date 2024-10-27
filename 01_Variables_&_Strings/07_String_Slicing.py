#Slicing is the accessing parts of a string
name="python is high level language"
print(name[0:6])     #python     from    [0 to 6 index]
print(name[7:9])     #is         from    [7 to 9 index]
print(name[10:14])   #high       from    [10 to 14 index]
print(name[15:20])   #level      from    [15 to 20 index]
print(name[21:28])   #language   from    [21 to 28 index]

#add 0 index at the start of the string  automatically if not write:
print(name[ :6])      #python [is same as the 0 to 6 index]  
#[21 : len(of the string)] 
print(name[21: ])     #langauge [is same the 21 to 28 index]
#negative Slicing:
print(name[-1:-7])        #minus from the total length of the string 