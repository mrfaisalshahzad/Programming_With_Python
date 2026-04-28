#wap to ask the user to enter names of their 3 favorite movies and store them in a list
mov1 = input("Enter 1st movie: ")
mov2 = input("Enter 2st movie: ")
mov3 = input("Enter 3st movie: ")

mov_list = [mov1, mov2, mov3]
print(mov_list)

#wap to check if a list contains a palindrome of elements (Hint: se copy())
list1 = [1, 2, 3, 2, 1]
list2 = [1, 2, 3, 2, 4]

copy_list1 = list1.copy()
copy_list2 = list2.copy()

copy_list1.reverse()
copy_list2.reverse()

if(copy_list1 == list1):
    print("list 1 contains palindrome")
elif(copy_list2 == list2):
    print("list 2 contains palindrome")
else:
    print("all lists don't contains palindrome")


#wap to count the number of students with the "A" grade in the following tuple.tuple
grade = ("C", "D", "A", "A", "B", "B", "A")
print(grade.count("A"))

#Store the above values in a list & sort them from "A" to "D"
list = ["C", "D", "A", "A", "B", "B", "A"]
list.sort()
print(list)