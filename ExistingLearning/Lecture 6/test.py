# write a recursive function to print the elements of a list in a single line. (list is the parameter)

marks = [94.4, 87.5, 95.2, 66.4, 45.1]

def print_element(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx], end= " ")
    print_element(list, idx+1)

print_element(marks)
print()