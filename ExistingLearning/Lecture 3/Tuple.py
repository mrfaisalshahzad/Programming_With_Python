#A bilit-in data type that lets us crate immutable sequences of values

# How to define Tuple
"""
Diff between List and Tuple

List: all values are Homogeneous i.e. similar meaning
Lists are Mutable
Example: expense list exp = [12, 456, 654]

Tuple: all value are Hetrogeneous i.e. different meaning
Tuples are Immutable
Example: list of x & y coordinates point = (8,9)
"""

tup = (2, 3, 4, 5)
print(tup)
print(tup[0])
print(tup[3])


point = (5, 9)
x_value = point[0]
y_value = point[1]
print(x_value)
print(y_value)

# Try to change value of a point in Tuple and it will throw error
point[0] = 11
print(point)

# empty tuple
a = ()
print(a)
print(type(a))

#single value tuple
a = (1,)
#a = (1)  #python will consieter this as an integer value
print(a)
print(type(a))


#tuple slicing
tup = (2, 3, 4, 5)
print(tup[1:3])
print(tup[1:])
print(tup[:len(tup)])
print(tup[:3])


#tuple methods

#tup.index(el)  returns index of first occurrence
tup = (2, 3, 2, 5)
print(tup.index(2))

#tup.count(el)  counts total occurrences
tup = (2, 3, 2, 5)
print(tup.count(2))

# major meethods of tuple with their description:
