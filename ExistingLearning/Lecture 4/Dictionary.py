#dictionaries are used to store data values in key:value pairs
#They are unordered, mutable (changeable) & don't allow duplicate keys

# Defining  a Dictionary
"""
d = {"tom":4654654, "joe":189464, "flip":35469646}
print(d)
"""

#Empty dictionary

d = {}

print(type(d))

# Accessing a key in dictionary
"""
d = {"tom":4654654, "joe":189464, "flip":35469646}
d = d["tom"]
print(d)
"""

# Changing value of a  Key in Dictionary
"""
d = {"tom":4654654, "joe":189464, "flip":35469646}
d["tom"] = 4765765
print(d)
"""

# Deleting a Key from Dictionary
"""
d = {"tom":4654654, "joe":189464, "flip":35469646}
del d["tom"]
print(d)
"""

# Print evey Key and its Value in Dictionary
"""
d = {"tom": 4654654, "joe": 189464, "flip": 35469646}
for key in d:
    print("Key", key, "value", d[key])
"""

# Another way to access Keys and Values in dictionaries
"""
d = {"tom":4654654, "joe":189464, "flip":35469646}
for k, v in d.items():
    print("key", k, "value", v)
"""

# Check a specific Key in Dictionary
"""
d = {"tom":4654654, "joe":189464, "flip":35469646}
result1 = "tom" in d
result2 = "sameer" in d
print(result1)
print(result2)
"""

# How to trash all the entries in Dictionary
"""
d = {"tom":4654654, "joe":189464, "flip":35469646}
d.clear()
print(d)
"""

# Nested Dictionaries

student = {
    "name" : "faisal shahzad",
    "subjects" : {
        "phy" : 97,
        "chem" : 75,
        "mat" : 87
    }
}

print(student)
print(student["subjects"])
print(student["subjects"]["phyc"])


# Dictionary Methods

# mydict.keys()  returns all keys
student = {
    "name" : "faisal shahzad",
    "subjects" : {
        "phy" : 97,
        "chem" : 75,
        "mat" : 87
    }
}

print(student.keys())
print(list(student.keys()))
print(len(student))
print(len(list(student.keys())))

# mydict.values()  returns all values
student = {
    "name" : "faisal shahzad",
    "subjects" : {
        "phy" : 97,
        "chem" : 75,
        "mat" : 87
    }
}

print(student.values())
print(list(student.values()))


# mydict.items()  returns all (key, val) pairs as tuples
student = {
    "name" : "faisal shahzad",
    "subjects" : {
        "phy" : 97,
        "chem" : 75,
        "mat" : 87
    }
}

print(student.items())
print(list(student.items()))
pairs = list(student.items())
print(pairs[1])

#mydict.get("key")  returns the key according to value
student = {
    "name" : "faisal shahzad",
    "subjects" : {
        "phy" : 97,
        "chem" : 75,
        "mat" : 87
    }
}

print(student["name"])
print(student.get("name"))
print(student["name2"])  #returns error if key is not available
print(student.get("name2"))  #returns no error -> None


#mydict.update(newdict)  inserts the specified items to the dictionary
student = {
    "name" : "faisal shahzad",
    "subjects" : {
        "phy" : 97,
        "chem" : 75,
        "mat" : 87
    }
}

student.update({"city" : "riyadh", "age" : 18})  #if updated with same key and different value, then it will replace orignal value of the key.
print(student)