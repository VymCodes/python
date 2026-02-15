base = int(input("Enter a base number : "))
exp = int(input("Enter a exponent : "))
default = 1
x = 0

while x < exp:
    default = default * base
    x += 1

print(f"The answer is {default}")