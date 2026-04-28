#A built-in data type that stores a set of values
#it canstore elements of different types  (integer, float, string, etc)
#Lists are mutable (changeable)
#Strings are immutable (non changable)

marks = [94.4, 87.5, 95.2, 66.4, 45.1]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(len(marks))

student = ["faisal", 95.4, 17, "Riyadh"]
print(student)


#list slicing

marks = [94.4, 87.5, 95.2, 66.4, 45.1]
print(marks[1:4])
print(marks[1:])
print(marks[:4])
print(marks[:len(marks)])


#list methods

#list.append(4)  adds one element at the end
marks = [94.4, 87.5, 95.2, 66.4, 45.1]
marks.append(25.6)
print(marks)

#list.sort()  sorts in ascending order
marks = [94.4, 87.5, 95.2, 66.4, 45.1]
print(marks.sort())  #returns None because it making changes ot orignal string
marks.sort()
print(marks)

#list.sort(reverse = True)  sorts in decending order
marks = [94.4, 87.5, 95.2, 66.4, 45.1]
print(marks.sort(reverse = True))  #returns None because it making changes ot orignal string
marks.sort(reverse = True)
print(marks)

#list.reverse()  reverses list
marks = [94.4, 87.5, 95.2, 66.4, 45.1]
list = ["apple", "banana", "strawbery", "cherry"]
marks1.reverse()
marks2.reverse()
print(marks)
print(list)

#list.insert(idx, el)  insert element at a specific index
list = ["apple", "banana", "strawbery", "cherry"]
list.insert(2, "kiwi")
print(list)

#list.remove(1)  removes first occurence of element
list = ["apple", "banana", "strawbery", "appple", "cherry"]
list.remove("apple")
print(list)

#list.pop(idx)  removes element at idx
list = ["apple", "banana", "strawbery", "appple", "cherry", "apple"]
list.pop(4)
print(list)


# important list methods with short descriptions:

# append(el) - adds an element to the end of the list
# sort() - sorts the list in ascending order
# sort(reverse=True) - sorts the list in descending order
# reverse() - reverses the order of the list
# insert(idx, el) - inserts an element at a specific index
# remove(el) - removes the first occurrence of an element
# pop(idx) - removes the element at a specific index
# extend(iterable) - extends the list by appending elements from an iterable
# clear() - removes all elements from the list
# count(el) - returns the number of occurrences of an element in the list
# index(el) - returns the index of the first occurrence of an element in the list
# copy() - returns a shallow copy of the list
# len(list) - returns the number of elements in the list
# list[idx] - accesses the element at a specific index
# list[start:end] - returns a slice of the list from start index to end index (exclusive)
# list[start:] - returns a slice of the list from start index to the end of the list
# list[:end] - returns a slice of the list from the beginning to end index (exclusive)
# list[:] - returns a copy of the entire list
# list1 + list2 - concatenates two lists
# list * n - repeats the list n times
# in operator - checks if an element is in the list
# not in operator - checks if an element is not in the list
# list comprehension - a concise way to create lists using a single line of code
# list.sort() - sorts the list in place (modifies the original list)
# sorted(list) - returns a new sorted list without modifying the original list
# list.reverse() - reverses the order of the list in place (modifies the original list)
# reversed(list) - returns an iterator that accesses the elements of the list in reverse order without modifying the original list
# list.copy() - returns a shallow copy of the list (creates a new list with the same elements)
# list.clear() - removes all elements from the list (modifies the original list)
# list.count(el) - returns the number of occurrences of an element in the list
# list.index(el) - returns the index of the first occurrence of an element in the list
# list.insert(idx, el) - inserts an element at a specific index (modifies the original list)
# list.remove(el) - removes the first occurrence of an element from the list (modifies the original list)
# list.pop(idx) - removes the element at a specific index and returns it (modifies the original list)
# list.extend(iterable) - extends the list by appending elements from an iterable (modifies the original list)
# len(list) - returns the number of elements in the list
# list[idx] - accesses the element at a specific index
# list[start:end] - returns a slice of the list from start index to end index (exclusive)
# list[start:] - returns a slice of the list from start index to the end of the list
# list[:end] - returns a slice of the list from the beginning to end index (exclusive)
# list[:] - returns a copy of the entire list
