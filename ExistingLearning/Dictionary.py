# Defining  a Dictionary
"""
d = {"tom":4654654, "joe":189464, "flip":35469646}
print(d)
"""

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
