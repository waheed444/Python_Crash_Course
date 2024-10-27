# File I/O in Python
# Python can be used to perform operations on a file. (read & write data)
# Types of all files
# 1.Text Files : .txt, .docx, .log etc.
# 2 Binary Files : .mp4, .mov, .png, .jpeg etc.
#Open,Read,Write and Close the file.
#read file
f = open("demo.txt","r")
data = f.read()
print(data)
print(type(data))
f.close()

#  Here are the meanings of the alphabetic file modes in Python:
# 'r': Read mode (default) - Opens the file for reading only.
# 'w': Write mode - Opens the file for writing (truncates if exists, creates if not).
# 'a': Append mode - Opens the file for writing (creates if not exists, pointer at end).
# 'x': Exclusive creation mode - Creates a new file (fails if exists).
# 'b': Binary mode - Opens the file in binary mode (used for non-text files).
# 't': Text mode (default) - Opens the file in text mode (used for text files).
# '+': Updating mode - Opens the file for both reading and writing.

f = open("demo.txt","r")
data = f.read(5) #read the first 5 characters of the line
print(data)
f.close()

f = open("demo.txt","r")
f.readline()   #read the text line by line 
line2 = f.readline()   #read the particular line
print(line2)
f.close()

# wrrite file
f=open("demo.txt","w")
f.write("I want to modify the data in txt file using f.write ")
f.close()
#append data
f=open("demo.txt","a")
f.write("I want to modify the data in txt file using f.write and i am also using append fuction over write function ")
f.close() 

# "r+" file
f=open("demo.txt","r+")
f.write("r+ is add text in start ")
f.close()