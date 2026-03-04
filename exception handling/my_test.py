try:
    num1 = int(input("Enter the number you would like : "))
    num2 = int(input("Enter another number : "))
    result = num1 * num2 
    print(f"These 2 numbers numtiplied is {result}")

except ValueError as ex:
    print("Please enter 2 numbers")