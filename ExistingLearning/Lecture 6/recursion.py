#Recursion is a function that calls itself repeatedly until a condition is met.
# def show(n):
# if(n == 0):
#    return
#print(n)
#show(n-1)

#Recursion function follows call stack process.
#Call stack is a stack data structure that stores information about the active subroutines of a computer program.

def show(n):
    if(n==0):  #base case
        return
    print(n)
    show(n-1)
    #print("end")

show(5)


# Factorial(n!) of 5! = 4! * 5
#n! = (n-1)! * n

def fact(n):
    if(n == 1 or n == 0):
        return 1
    return fact(n-1) * n

print(fact(4))