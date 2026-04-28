#waf to print the length of a list (list is the parameter)

cities = ["a", "b", "c", "d", "e"]

def print_len(list):
    print(len(list))
    return len(list)

print_len(cities)


#waf to print the elements of a list in a single line. (list is the parameter)

students = ["Ali", "Ahmed", "Asad", "Adil"]

def print_ele(list):
    for ele in list:
        print(ele, end= " ")
        
print_ele(students)
print()


#waf to find the factorial fo n. (n is the parameter)
number = 5

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)
        

factorial(number)


#waf to convert USD to INR. (USD is the parameter)

USD = 75

def convert(USD, INR = 83):
    a = USD * INR
    print(USD, "USD = ", a, "INR")

convert(USD)


#waf to check if a number is odd or even. (number is the parameter)

number = 22

def odd_even(n):
    if(n%2 == 0):
        print(n, "is even")
    else:
        print(n, "is odd")
    
odd_even(number)


# waf to calculate the sum of n natural numbers. (n is the parameter)

def cal_sum(n):
    if(n == 0):
        return 0
    return cal_sum(n-1) +n

print(cal_sum(5))


# write a recursive function to print the elements of a list in a single line. (list is the parameter)

marks = [94.4, 87.5, 95.2, 66.4, 45.1]

def print_element(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx], end= " ")
    print_element(list, idx+1)

print_element(marks)
print()