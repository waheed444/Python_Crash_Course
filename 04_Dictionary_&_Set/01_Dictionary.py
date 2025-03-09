#Dictionaries are ordered collection of data items. 
# They store multiple items in a single variable. 
# Dictionary items are key-value pairs 
# that are separated by commas and enclosed within curly brackets {}.

dic = {'name':'waheed', 'age':21, 'eligible':True}
print(dic)

#Accessing multiple values:

dic = {'name':'ahmad', 'age':19, 'eligible':True}
print(dic['name'])
print(dic.get('eligible'))


dic = {'name':'waheed', 'age':21, 'eligible':True}
print(dic.values())

dic = {'name':'ahmad', 'age':19, 'eligible':True}
print(dic.keys())



