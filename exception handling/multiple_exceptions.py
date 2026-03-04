name = input("Enter your name : ")
try:
    num1, num2 = eval(input(f"{name}, Enter two numbers, seperated by a comma : "))
    result = num1 / num2
    print(f"Result is {result}")

except ZeroDivisionError:
    print(" HAHAHAHAH Division by zero is error")

except SyntaxError:
    print("Comma is missing, READ THE QUESTION ")

except:
    print("Wrong input")

else:
    print("no exceptions")

finally:
    print("This will execute no matter what")