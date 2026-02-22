a = int(input("Enter your first number : "))
b = int(input("Enter your second number : "))

def add (a,b):
    return a + b

def sub (a,b):
    return a - b

def multi (a,b):
    return a * b

def div (a,b):
    return a / b

def power (a,b):
    return a ** b

print("Choose one operation from below ")
print("Option 1, add")
print("Option 2, subtract")
print("Option 3, multiply")
print("Option 4, divide")
print("Option 5, power")

choice= int(input("You selected Option : "))
if choice == 1:
    print(add(a,b))
elif choice == 2:
    print(sub(a,b))
elif choice == 3:
    print(multi(a,b))
elif choice == 4:
    print(div(a,b))
elif choice == 5:
    print(power(a,b))

