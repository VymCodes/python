num_1 = int(input("Enter your numerator : "))
num_2 = int(input("Enter your denomerator : "))

if num_1 % num_2 == 0:
    print(f"{num_1} is divisible by {num_2}")
else:
    print(f"{num_1} is not divisible by {num_2}")