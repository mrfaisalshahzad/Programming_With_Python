
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

point = (5, 9)
x_value = point[0]
y_value = point[1]
print(x_value)
print(y_value)

# Try to change value of a point in Tuple and it will throw error
point[0] = 11
print(point)