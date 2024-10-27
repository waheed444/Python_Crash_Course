#Dictionaries are ordered collection of data items. 
# They store multiple items in a single variable. 
# Dictionary items are key-value pairs 
# that are separated by commas and enclosed within curly brackets {}.

info = {'name':'waheed', 'age':21, 'eligible':True}
print(info)

#Accessing multiple values:

info = {'name':'ahmad', 'age':19, 'eligible':True}
print(info['name'])
print(info.get('eligible'))


info = {'name':'waheed', 'age':21, 'eligible':True}
print(info.values())

info = {'name':'ahmad', 'age':19, 'eligible':True}
print(info.keys())



