# Set is the collection of the unordered items.
#Eash element is the set must be unique & immutable.

collection = {1, 2, 3, 4, 4, "faisal shahzad", ("apple", "banana"), "faisal shahzad"}

print(collection)
print(type(collection))
print(len(collection))  #total number of items


#Empty Set
null_set = set()

print(type(null_set))


#Set Methods

#set.add(el)  adds an element
collection = set()

collection.add(1)
collection.add(2)
collection.add(2)
collection.add((1,2,3))
#3collection.add([1, 2, 3])  #it will give unhashable type: 'list' error

#collection.remove(3)  # it will give a key error like keys in dictionaries

print(collection)


#set.remove(el)  removes the element
collection = {1, 2, 3, 4}
collection.remove(1)

print(collection)


#set.clear()  empties the set
collection = {1, 2, 3, 4}
collection.clear()

print(len(collection))


#set.pop()  removes a random value
collection = {1, 2, 3, 4, "hello", "faisal", "shahzad"}

print(collection.pop())


#set.union(set2)  combines both set values and returens new
set1 = {1, 2, 3, 4}
set2 = {1, 2, 3, 5}

print(set1.union(set2))

#set.intersection(set2)  combines common values and returns new
set1 = {1, 2, 3, 4}
set2 = {1, 2, 3, 5}

print(set1.intersection(set2))