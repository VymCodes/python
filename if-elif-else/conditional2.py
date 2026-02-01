# a = [1,2,3,4,5]
# b = [1,2,3,4,5,6,7,8,9,10]
# c = 7

# print(a in b)
# print(a == b)
# print(c in a)
# print(c in b)
# print(c not in a)

# x = 4.1
# if type(x) is int:
#     print("X is a number")
# elif type(x) is float:
#     print("X is a decimal")
# elif type(x) is bool:
#     print("X is a boolean value")
# elif type(x) is str:
#     print("X is a string")

math = int(input("Enter score for maths : "))
science = int(input("Enter score for science : "))
if (90 < math < 100) and science < 60:
    print("You can take engineering, but not science")
elif math < 90 and science > 90:
    print("You cant be a mathematician, but you can be a scientist")
elif (0 < math < 50) and (0 < science < 50):
    print("You cant get a job")
elif math == 100 or science == 100:
    print("You are very smart, you can pick anything")
elif math == 0 or science == 0:
    print("Something is wrong")