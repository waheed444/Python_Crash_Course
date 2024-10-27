#Dictionary uses several built-in methods for manipulation.They are listed below
#We can access dictionary items by their key or by their value

info = {'name':'waheed', 'age':21, 'eligible':True}
print(info.values())   #by values

info = {'name':'ahmad', 'age':19, 'eligible':True}
print(info.keys())    #by key

#update Method

info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)
info.update({'age':20})
info.update({'DOB':2001})
print(info)

#clear():
# Remove all the value from the dictionary

info = {'name':'Karan', 'age':19, 'eligible':True}
info.clear()
print(info)

#The pop() method removes the key-value pair whose key is passed as a parameter.
#pop()

info = {'name':'Karan', 'age':19, 'eligible':True}
info.pop('age')
print(info)


#popitem():
# The popitem() method removes the last key-value pair from the dictionary.

info = {'name':'Karan', 'age':19, 'eligible':True}
info.popitem()
print(info)

#del:
# we can also use the del keyword to remove a dictionary item.

info = {'name':'Karan', 'age':19, 'eligible':True}
del info['name']
print(info)
