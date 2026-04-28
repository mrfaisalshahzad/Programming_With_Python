#Range functions return a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
#range(start?, stop, step?)

seq = range(10)

for val in seq:
    print(val)


for val in range(10):
    print(val)


for val in range(2, 10, 2):
    print(val)


#Pass statement
#Pass is a null statement that does nothing, it is used as a placeholder for future code.

#for el in range(10):
    #pass

for i in range(5):
    pass

print("someting useful")