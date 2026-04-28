#for loops are used for sequential traversal. For traversing list string, tuples ets
#for el in list:


"""
bad example

exp = [2340, 2500, 2100, 3100, 2980]
total = exp[0] + exp[1] + exp[2] + exp[3] + exp[4]
print("total is :", total)
"""

"""
use of For loop

exp = [2340, 2500, 2100, 3100, 2980]
total = 0
for item in exp:
    total = total + item
print(total)
"""

"""
Using range in for loop

for i in range (1,11):
    print(i, pow(i, 2))

exp = [2340, 2500, 2100, 3100, 2980]
for i in range(len(exp)):
    print(i)
"""

"""
Using range and len in For loop

exp = [2340, 2500, 2100, 3100, 2980]
total = 0
for i in range(len(exp)):
    print("Month", (i+1), "expense", exp[i])
    total = total + exp[i]
print("Total expense is", total)
"""

"""
Use of Break in For loop

key_location = "chair"
locations = ["garage", "kitchen", "closet", "chair"]
for i in locations:
    if i == key_location:
        print("key is found in ", i)
        break
    else:
        print("key is not found in ", i)
"""
"""
Use of Continue in For loop

for i in range(1,6):
    if i % 2 == 0:
        continue
    print(i)
"""

"""
Use of While loop (you have manually increment the variable)
"""
i = 1
while i <= 5:
    print(i)
    i = i +1


#use of for loop in list/tuple/character
list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for val in list:
    print(val)



str = "Faisal Shahzad"

for char in str:
    if(char == "l"):
        break
    else:
        print(char)

print("end of loop")


#using Break or continue in for loop 
list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
n = int(input("Enter number :"))

for val in list:
    if(n == val):
        print("number found at idx", list.index(val))
        break
    else:
        print("finding...")

