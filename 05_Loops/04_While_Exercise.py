# #print numbers from 1 to 100 in
# count=1
# while(count<=100):
#     print(count)
#     count+=1
# #print numbers from 1 to 100 in reverse order (100 to 1)    
# count=100
# while(count>=1):
#     print(count)
#     count-=1
    
# # #print the multiplication table of n number 
# # n=int(input("Enter any number to make the table  :"))
# i=1
# while(i<=10):
#     print(n,"x",i,"=",n*i)
#     i+=1      
    
# Print the elements of the following list using a loop:
number=[1, 4, 9, 16, 25, 36, 49, 64, 81,100]
idx=0                 #idx is the index varaible of the given list
while(idx<len(number)):
    print(number[idx])
    idx+=1

#Search for a number x in this tuple using loop:
number=[1, 4, 9, 16, 25, 36, 49, 64, 81,100]
x=36
i=0
while(i<len(number)):
    if(number[i]==x):
        print("Found at the index",i)
    i+=1
