#store following word meanings in a python dictionary
mydict = {
    "table" : ("a piece of furniture", "list of facts & figures"),
    "table" : ["a piece of furniture", "list of facts & figures"],
    "cat" : "a small animal"
}

print(mydict)


#you are given a list of subjects for students. assume one classromm is required for 1 subject. how many classromms are needed by all students.
subjects = {"python", "java", "c++", "python", "javascript", "java", "python", "java", "c++", "c"}

print("Classrooms required: ", len(subjects))


#wap to enter marks of 3 subjects form the user and store them in a dictionary. start with an empty dictionary and add one by one.
# use subject names as key and marks as value.
mydict = {}

subject1 = input("Please enter 1st subject name: ")
marks1 = int(input("Please enter marks: "))
mydict.update({subject1 : marks1})

subject2 = input("Please enter 2nd subject name: ")
marks2 = int(input("Please enter marks: "))
mydict.update({subject2 : marks2})

subject3 = input("Please enter 3rd subject name: ")
marks3 = int(input("Please enter marks: "))
mydict.update({subject3 : marks3})

print(mydict)


#Figure out a way to store 9 & 9.0 as separate values in the set (you can take help of built-in data types)
values1 = {("float", 9.0), ("int", 9)}
values2 = {9, "9.0"}

print(values1)
print(values2)