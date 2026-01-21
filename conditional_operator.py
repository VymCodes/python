# x = int(input(" Enter a number for X : "))
# y = int(input(" Enter a number for Y : "))
# z = int(input(" Enter a number for Z : "))

# if x and y and z :
#     print("None of these numbers are 0")
# else :
#     print("At least one of these numbers are zero")

# if x or y or z :
#     print("At least one of them is not 0")
# else:
#     print("all of them are 0")

# if (x == y) and (y == z) :
#     print("All three of these numbers are equal")
# elif (x != y) and (y != z):
#     print (" None of these numbers are equal")
# elif (x == y) and (y != z):
#     print("Only x and y are equal")
# elif (x != y) and (y == z):
#     print("Only y and z are equal")

# if (x > y) and (x > z):
#     print("X is the greatest")
# elif (y > x) and (y > z):
#     print("Y is the greatest")
# elif (z > x) and (z > y):
#     print("Z is the greatest")

height = float(input("Enter your height in meters : "))
weight = float(input("Enter your weight in kilograms : "))

bmi = weight / (height ** 2)
if bmi <= 18.4:
    print("You are underweight")
elif bmi <= 24.9:
    print("You are healthy")
elif bmi <= 29.9:
    print("You are overweight")
else:
    print("You are obese")
