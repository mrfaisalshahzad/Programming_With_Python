#str.endswith("er")  returns true is string ends with substr

str = "Faisal Shahzad"
print(str.endswith("ad"))


#str.capitalize()  capitalizes 1st char

str = "saisal shahzad"
print(str.capitalize())  #its a new string it didn't change the orignal string

str = "faisal shahzad"
str = str.capitalize()  #this stores changes in orignal stirng
print(str)


#str.replace(old, new)  replaces all occurrences of old with new

str = "faisal shahzad"
print(str.replace("a", "o"))
print(str.replace("faisal", "sajid"))


#str.find(word)  returns 1st index of 1st occurrence

str = "faisal shahzad"
print(str.find("a"))
print(str.find("shahzad"))
print(str.find("q"))  #when someting doesn't exist then ans is -1 is not avalid index. -ve indexes are only for slicing strings


#str.count("am")  counts the occurrence of substr in string

str = "faisal shahzad"
print(str.count("a"))
print(str.count("fasial"))