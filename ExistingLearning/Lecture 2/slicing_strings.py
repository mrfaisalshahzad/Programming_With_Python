#Accessing parts of string is called slicing

#str [starting_idx : ending_idx]  ending idx is not included

#+ve indexing

str = "Faisal Shahzad"

print(str[1:4])
print(str[1:7])


#-ve indexing

print(str[-4:-1])
print(str[-7:-1])
print(str[-len(str):-1])
print(str[:-1])

# common string methods with short description:

# str.lower() - converts string to lowercase
# str.upper() - converts string to uppercase
# str.strip() - removes leading and trailing whitespace
# str.replace(old, new) - replaces occurrences of old with new
# str.split(delimiter) - splits the string into a list using the specified delimiter
# str.join(iterable) - joins elements of an iterable into a string, separated by the string on which it is called
# str.find(sub) - returns the lowest index of the substring if found, otherwise returns -1
# str.startswith(prefix) - returns True if the string starts with the specified prefix, otherwise False
# str.endswith(suffix) - returns True if the string ends with the specified suffix, otherwise False
# str.isalpha() - returns True if all characters in the string are alphabetic, otherwise False
# str.isdigit() - returns True if all characters in the string are digits, otherwise False
# str.isalnum() - returns True if all characters in the string are alphanumeric, otherwise False
# str.count(sub) - returns the number of occurrences of the substring in the string
# str.format(*args, **kwargs) - formats the string using the specified arguments
# str.rfind(sub) - returns the highest index of the substring if found, otherwise returns -1