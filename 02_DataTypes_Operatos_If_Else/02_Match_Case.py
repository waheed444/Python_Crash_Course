# Match case is very imp feature avaialbe in python 3.10 and above
#match case is just like the switch case  in c/c++
x = int(input("Enter any number :"))
print("You are enter   :",x)
#match statement is stated
match x:
        #underscore '_' is very imp in syntax of case 
        case _ if x<0:
         #if condition statement is used to make the case in match statement                               
          print("The value of x is negative")
        case _ if x==0:
          print("The value of x is 0")    
        case _ if x>0:
          print("The value of x is postive")
        #Unlike in C/C++,there is no break statement used in python 
        #when the required case is true the prgram automatically terminated.
        


