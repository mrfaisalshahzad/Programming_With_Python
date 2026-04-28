#Create a file named practice.txt and write the following lines in it:

f = open("LearnPython/Lecture 7/practice.txt", "w")
f.write("Hi everyone\nwe are learning File I/O\n")
f.write("\nusing Java.\nI like programming in Java.")
f.close()

f = open("LearnPython/Lecture 7/practice.txt", "r")
data = f.read()
print(data)
f.close()


#waf that replaces all occurences of Java in a string with Paython
f = open("LearnPython/Lecture 7/practice.txt", "r")
str = f.read()

new_str = str.replace("Java", "Python")
print(str)

f = open("LearnPython/Lecture 7/practice.txt", "w")
f.write(new_str)

f = open("LearnPython/Lecture 7/practice.txt", "r")
str = f.read()
print(str)
f.close()



# wap to check if the word "learning" is present in the file or not

f = open("LearnPython/Lecture 7/practice.txt", "r")
data = f.read()
word = "learning"
if(data.find(word) != -1):
    print("Yes")
else:
    print("No")
f.close()


#wap to check if the word "programming" is present in the file or not. If yes, print the line number.
def checkforline():
    word = "programming"
    data = True
    line_no = 1
    with open("LearnPython/Lecture 7/practice.txt", "r") as f:
        while data:
            data = f.readline()
            if word in data:
                print(line_no)
                return
            line_no += 1
    return -1
print(checkforline())



#wap to count the number of even numbers in the file

f = open("LearnPython/Lecture 7/practice1.txt", "w")
f.write("1, 2, 76, 84, 90, 101")

with open("LearnPython/Lecture 7/practice1.txt", "r") as f:
    data = f.read()
    print(data)


# num = ""
# for i in range(len(data)):
#     if(data[i] == ","):
#         print(num.strip()) # Print number without leading or trailing spaces
#         num = ""
#     else:
#         num += data[i]

# if num.strip(): # Print the last number
#     print(num.strip())

count = 0
num = data.split(", ")
for val in num:
    if(int(val) % 2 == 0):
        count += 1
print(count)
