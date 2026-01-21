x = int(input(" Enter a number for X : "))
y = int(input(" Enter a number for Y : "))
z = int(input(" Enter a number for Z : "))

if x and y and z :
    print("None of these numbers are 0")
else :
    print("At least one of these numbers are zero")

if x or y or z :
    print("At least one of them is not 0")
else:
    print("all of them are 0")