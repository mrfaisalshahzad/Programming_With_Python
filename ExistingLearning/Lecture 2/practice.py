#get name input and print it and its length
first_name = input("Enter First Name: ")
print("First Name: ", first_name)
print("length: ", len(first_name))


#find count of $ in a string
Amount = "Amount in $: "
print(Amount.count("$"))


#wpa if a number entered by a user is odd or even
number = int(input("Enter number: "))

if(number % 2  == 0):
    print("Number is = Even")
else:
    print("Number= Odd")

print("End of Code")


#wap to find the greatest fo 3 numbers entered by the user.
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))

if(a >= b and a >= c):
    print("1st numbr is largest")
elif(b >= c):
    print("2nd number is largest")
else:
    print("3rd number is largest")


#wap to chedi if a number is a multiple of 7  or not.
a = int(input("Enter number: "))

if(a % 7 == 0):
    print("number is a multipule of 7")
else:
    print("number is not multiple of 7")