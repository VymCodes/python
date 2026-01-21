# age = int(input("enter your age : "))
# print(f"your age is {age}")
# print(type(age))
# if age >= 18:
#     print("You can vote")
# else:
#     print("You are too young to vote")

# score = int(input("Enter your score : "))
# print(f"your score is {score}%")
# if score >= 80:
#     print("You got an A!")
# elif score >= 60:
#     print("You got an B!")
# elif score >= 40:
#     print("You got a C!")
# elif score >= 20:
#     print("You got a D")
# else:
#   print("F,You have failed horribly")


selling_price = int(input("Enter your selling price of a iphone : "))
making_price = int(input("Enter your making price of a phone : "))
if selling_price - making_price > 0:
    print("Good job! You made profit")
elif selling_price == making_price:
    print("We made no profit")
else:
    print("Wow, you lost all our money")