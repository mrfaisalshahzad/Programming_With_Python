#Print numbers from 1 to 100
i = 1

while i <= 100 :
    print(i)
    i += 1

print("loop ended")


#Print numbers from 100 to 1
i = 100

while i >= 1 :
    print(i)
    i -= 1

print("loop ended")

#Print the multiplication table of n
n = int(input("Enter number: "))
i = 1

while i <= 10 :
    print(n, "*", i, "=", " ", n * i)
    i += 1

print("loop ended")


#Print the elements of the following list using a loop [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
i = 1
increment = 3

while i <= 100 :
    print(i)
    i = i + increment
    increment += 2

print("loop ended")

### usind list index
list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
idx = 0

while idx <= len(list) :
    print(list[idx])
    idx += 1

print("end of code")


#Search for a number x in this tuple using loop [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
n = int(input("Enter a number :"))
idx = 0

while idx < len(list) :
    if(n == list[idx]) :
        print("Number found at idx", idx)
    else:
        print("finding..")
    idx += 1

print("end of code")


#Break
list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
n = int(input("Enter a number :"))
idx = 0

while idx < len(list) :
    if(n == list[idx]) :
        print("Number found at idx", idx)
        break
    else:
        print("finding..")
    idx += 1

print("end of loop")


#Continue
i = 1

while i <= 5 :
    if(i == 3):
        i += 1
        continue
    print(i)
    i += 1


i = 1

while i <= 10 :
    if(i % 2 == 0):
        i += 1
        continue
    print(i)
    i += 1


i = 1

while i <= 10 :
    if(i % 2 != 0):
        i += 1
        continue
    print(i)
    i += 1

#Range

for i in range(1,101):
    print(i)

for i in range(100, 0, -1):
    print(i)

#table
n = int(input("Enter number"))

for i in range(1, 11):
    print(i , "*", n, "=", i * n)


#Pass
for i in range(5):
    pass

print("someting useful")



#wap to find the sum of  natural numbers useing for loop

n = 7
sum = 0

for i in range(1, n+1):
    sum += i 

print("Total is ", sum)


#wap to find the sum of  natural numbers useing while loop

n = 7
sum = 0
i = 1

while i <= n:
    sum += i
    i += 1

print("Total is ", sum)


#wap for find the factorial of first n numbers using For loop

n = 7
fact = 1

for i in range(1, n+1):
    fact *= i  #fact = fact * i

print("Factorial of", n, "is =", fact)


#Create a program to print the following pattern

set = ""

for i in range(0, 11, 1):
    if(i <= 11):
        set += str(i) + " "
        print(set)