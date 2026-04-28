#Python can be used to perfom operations on a file like reading, writing, appending, etc.
#Types of all files
#1. Text File
#2. Binary File

#Open, read & close a file

# f = open("file_name", "mode")
# data = f.read()
# f.close()

f = open("LearnPython/Lecture 7/demo.txt", "rt") #t is for text mode and its default mode
data = f.read()
print(data)
print(type(data))
f.close()

#'r' - read mode (default)
#'r+' - read and write mode (pointer at the beginning of the file and it overwrites the file. if the file exists then it will not create a new file else it will create a new file)
#'w' - write mode (truncates the file first means it will delete all the data in the file) overwites mode.
#'w+' - write and read mode (truncates the file first means it will delete all the data in the file) overwites mode.
#'x' - exclusive creation mode, it creates a new file and opens it for writing. If the file already exists, the operation fails.
#'a' - append mode, it opens the file for writing at the end of the file without truncating it. It creates a new file if it does not exist.
#'a+' - append and read mode, it opens the file for reading and writing at the end of the file without truncating it. It creates a new file if it does not exist.
#'b' - binary mode
#'t' - text mode (default)
#'+' - read and write mode (opens a file for updating i.e., reading and writing)

#Reading a file

# data = f.read() #reads the entire file

# data = f.read(5) #reads the first 5 characters of the file

f = open("LearnPython/Lecture 7/demo.txt", "r")
data = f.read(5)
print(data)
print(type(data))
f.close()

# data = f.readline() #reads the first line of the file

f = open("LearnPython/Lecture 7/demo.txt", "r")
data = f.readline()
print(data)
print(type(data))
f.close()


f = open("LearnPython/Lecture 7/demo.txt", "r")
line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)

line3 = f.readline()
print(line3)

line4 = f.readline()
print(line4)
f.close()


#Writing a file
f = open("LearnPython/Lecture 7/demo.txt", "a+")
# f.write("abc")
print(f.read())
f.write("abc") #appends the data at the end of the file
f.close()


#With Syntax
# with open("file_name", "mode") as f:
#     data = f.read()

with open("LearnPython/Lecture 7/demo.txt", "r") as f:
    data = f.read()
    print(data)
    print(type(data))

with open("LearnPython/Lecture 7/demo.txt", "w") as f:
    f.write("Hello World")

#Deleting a file
#Using the os module

#Module (like a code libarary) is a file containing a set of functions you want to include in your application.

# import os
# os.remove("file_name")

import os
os.remove("LearnPython/Lecture 7/demo.txt")