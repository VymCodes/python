my_number = str(input("Enter a number or alphabet : "))


if my_number.isdigit():
    print(f"'{my_number}' is a number")
elif my_number.isalpha():
    print(f"'{my_number}' is an alphabet")
else:
    print(f"'{my_number}' Please enter 1 number or alphabet)")