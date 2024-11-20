# Consider a module to be the same as a code library.
# A file containing a set of functions you want to include in your application.
# We can use the module we just created, by using the import statement:

import mymodule
mymodule.ShowName("WAHEED AHMAD")



# You can choose to import only parts from a module, by using the from keyword.

from mymodule import person1
print(person1['name'])
print(person1['age'])
print(person1['country'])