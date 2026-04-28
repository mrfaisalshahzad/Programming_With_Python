"""
num = input("Enter a number: ")
num = int(num)
if num % 2 == 0:
    print("number is even")
else:
    print("number is odd")
"""


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
