#if-elif-else (SANTAX)

#if(condition):
    #statement1
#elif(condition):
    #statement2
#else:
    #statementN

light = "Pink"

if(light == "Red"):
    print("Stop")
elif(light == "Yellow"):
    print("slowdown")
elif(light == "Green"):
    print("Go")
else:
    print("lignt is broken")

print("End of Code")


#if-elif and logical operators
marks = float(input("Enter students marks"))

if(marks >= 90):
    print("Grade= A")
elif(marks >= 80 and marks < 90):
    print("Grade= B")
elif(marks >= 70 and marks < 80):
    print("Grade= C")
else:
    print("Grade= D")

print("End of Code")


"""
num = input("Enter a number: ")
num = int(num)
if num % 2 == 0:
    print("number is even")
else:
    print("number is odd")
"""

'''
indian = ["samosa", "daal", "naan", "karahi"]
chinese = ["egg roles", "egg fried rice", "pot sticker"]
italian = ["pizza", "pasta", "risotto"]

dish = input("Enter a dish name: ")

if dish in indian:
    print("Indian")
elif dish in chinese:
    print("Chinese")
elif dish in italian:
    print("Italian")
else:
    print("Based on little knowledge I have, I don't know which cousin is this")
'''

