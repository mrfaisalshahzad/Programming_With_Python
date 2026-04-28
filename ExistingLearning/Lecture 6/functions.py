#Functions are block of statements that perform a specific task. Functions help reduce redundancy in code.
#def func_name(param1, param2,,):
#   some code
#   return value

#func_name(arg1, arg2,,)  #Calling a function
#Example of a function

def  calcSum(a, b):  #a, b are parameters
    sum = a + b
    print(sum)
    return sum

calcSum(10, 5)  #function call, and 10, 5 are arguments


#function definition
def calc_sum(a, b):  #parameters
    return a + b

sum = calc_sum(1, 2)  #function arguments
print(sum)



def print_hello():
    print("Hello")

print_hello()
print_hello()
print_hello()



def print_hello():
    print("Hello")

output = print_hello()
print(output)


#average of 3 numbers  # 2, 3, 4

def calcavg(a, b, c):
    sum = a + b + c
    avg = sum / 3
    print(avg)
    return avg

calcavg(98, 97, 95)


#Types of functions, builtin functions, and user-defined functions
#builtin functions eg. print(), input(), len(), type(), id(), etc

print("faiasl shahzad","adil shahzad", end= " ")  #sep = " " by default, end = " " means no new line
print("adil shahzad")  #end = "\n" by default
#print("faiasl shahzad","adil shahzad", sep = ",")


#Default parameters in functions
#Assigning a default value to a parameter, which is used when no argument is passed to the function.

def cal_prid(a=1, b=1):
    print(a * b)
    return a * b

cal_prid()


def cal_prid(a, b=8):
#def cal_prid(a=8, b):  non-default argument follows default argument means default argument should be at the end.
    print(a * b)
    return a * b

cal_prid(1)


"""
Here we are repeating coding lines

tom_exp_list = [2100, 3400, 2400]
joe_exp_list = [1200, 2300, 5000]

total = 0
for item in tom_exp_list:
    total = total + item
print("Tom's total expense is ", total)

total = 0
for item in joe_exp_list:
    total = total + item
print("Joe's total expense is ", total)
"""

"""
Defining function

def calculate_total(exp):
    total = 0
    for item in exp:
        total = total + item
    return total


tom_exp_list = [2100, 3400, 2400]
joe_exp_list = [1200, 2300, 5000]

tom_total = calculate_total(tom_exp_list)
joe_total = calculate_total(joe_exp_list)

print("Tom's total expense is ", tom_total)
print("Joe's total expense is ", joe_total)
"""

"""
Positional Arguments
Local vs Global Variables

def sum(a, b):
    print("a:", a)
    print("b:", b)

    total = a + b
    print("total inside function:", total)
    return total


n = sum(10, 5)
print("Total outside function: ", n)
"""


"""
Named Arguments

def sum(a, b):
    print("a:", a)
    print("b:", b)

    total = a + b
    print("total inside function:", total)
    return total


n = sum(b=5, a=6)
print("Total outside function: ", n)
"""


"""
# Default Arguments (should be defined in function argument like b=0)

def sum(a, b=0):

# This function takes two arguments which are integer and returns sum of them as an output.

    print("a:", a)
    print("b:", b)

    total = a + b
    print("total inside function:", total)
    return total


n1 = sum(10)
n2 = sum(10,5)
print("Total outside function: ", n1)
print("Total outside function: ", n2)
"""




"""
Functions taking parameter and argument
Parameter: input defined in a function
Argument: input value for a give parameter
"""

"""
def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("welcome aboard")


greet("Faisal", "Shahzad")
"""

"""
Functions either 
- performa a task
- or return a value
"""

"""
def greet(name):
    print(f"Hi {name}")

# This function is a better practice
def get_greeting(name):
    return f"Hi {name}"



greet("Faisal")
message = get_greeting("Faisal Shahzad")
print(message)
"""

"""
#All functions return "None" by default

def greeting(name):
    print(f"Hi {name}")

print(greeting("Faisal"))

"""

"""
# Using keyword arguments

def increment(number, by):
    return number + by


# result = increment(2, 1)
print(increment(2, by=1))
"""

"""
# Optional parameters (by=1 is a fixed parameter)
def increment(number, by=1):
    return number + by


# result = increment(2, 1)
print(increment(5))
"""

"""
# Pass Variable number of arguments to a function 

def multiply(*numbers):
    # print(numbers)
    total = 1
    for numbers in numbers:
        print(numbers)
        # total = total * numbers
        total *= numbers
    print(total)


multiply(2, 3, 4)
"""

"""
# Pass Variable number of arguments to a function another way
# Passing multiple keyword arguments
# The result of this is a dictionary

def save_user(**user):
    print(user)
    print("ID: " + str(user["id"]), "Name: " + user["name"], "Age: " + str(user["age"]))


save_user(id=1, name="faisal", age=22)
"""


# Exercise

def fizz_buzz(input):
    if input % 3 == 0 and input % 5 == 0:
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input


print(fizz_buzz(7))
