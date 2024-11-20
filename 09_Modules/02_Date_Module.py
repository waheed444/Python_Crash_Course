# A date in Python is not a data type of its own,
# but we can import a module named datetime to work with dates as date objects.

import datetime       # Import the datetime module and display the current date:
x = datetime.datetime.now()
print(x)

# The date contains year, month, day, hour, minute, second, and microsecond.

# Create your specfic date and time 
import datetime
x = datetime.datetime(2020, 5, 17)
print(x)