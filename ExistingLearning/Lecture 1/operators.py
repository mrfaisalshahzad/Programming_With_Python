#An operator is a symbol that performs a certain operation between operands.

#Arithmetic Operators (+,-,*,/,%,**)

a = 5
b = 2

sum = a + b
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)# % is called modulo
print(sum)


#Relational / comparisson Operators (==, !=, >,<,>=,<=)

a = 50
b = 20

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)


#Assignment Operators (=,+=,-=,*=,/=,%=,**=)

num = 10
#num = num + 10
num += 10
print("num : ", num)

num = 10
#num = num - 10
num -= 10
print("num : ", num)

num = 10
#num = num * 10
num *= 10
print("num : ", num)

num = 10
#num = num / 10
num /= 10
print("num : ", num)


#Logical Operators (not, and, or)

a = 50
b = 30

print(not False)
print(not True)
print(not (a > b))

val1 = True
val2 = True
val3 = False

print("AND operator : ", val1 and val2)
print("AND operator : ", val1 and val3)
print("OR operator : ", val1 or val3)

print("AND operator : ", (a == b) and (a > b))
print("OR operator : ", (a == b) or (a > b))