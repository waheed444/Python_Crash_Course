
# WAP to check if a list contains a palindrome of elements. (Hint: use copy( ) method)
#palindrome means the word,list or any sentence that remain same if it reverse itself
#like 1,2,1 reverse --> remains same 1,2,1 and like m a a m --> m a a m

list1=[1,2,1]
list2=[1,3,5]

copy_list=list1.copy()
copy_list.reverse()

if(copy_list==list1):
    print("This is panlindrome")
else:
    print("This is not panlindrome")
