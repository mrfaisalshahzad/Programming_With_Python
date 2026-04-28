#wap to count the number of even numbers in the file

f = open("LearnPython/Lecture 7/practice1.txt", "w")
f.write("1, 2, 76, 84, 90, 101")

with open("LearnPython/Lecture 7/practice1.txt", "r") as f:
    data = f.read()
    print(data)


# num = ""
# for i in range(len(data)):
#     if(data[i] == ","):
#         print(num)
#         num = ""
#     else:
#         num += data[i]

count = 0
num = data.split(", ")
for val in num:
    if(int(val) % 2 == 0):
        count += 1
print(count)
