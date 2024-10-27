#break statement terminates the loop when if condition is true

count=1
while(count<=10):
    print(count)
    count+=1
    if(count==6):  #(output will be 1 to 5 "6" not included here)
        break
print("Break")   
x=1 
while(x<=10):
    if(x==6):   #(print 1 to 10 and 6 not include in output)
        x+=1
        continue
    print(x)
    x+=1
    
fruits = ['apple', 'peach', 'banana', 'mango', 'orange']
for x in fruits:        # Start a loop that goes through each fruit in the list
    print(x)            # Print the current fruit
    if (x == 'mango'):    # Check if the current fruit is 'mango'
        break           # If it is, break out of the loop

fruits = ['apple', 'peach', 'banana', 'mango', 'orange']
for x in fruits:        # Start a loop that goes through each fruit in the list
    if (x == 'mango'):    # Check if the current fruit is 'mango'
        continue        # If it is, skip the rest of the loop and go to the next iteration
    print(x)            # Print the current fruit


