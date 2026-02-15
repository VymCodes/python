numb = int(input("enter a number to find the amount of digits : "))
x = 0

while numb != 0:
    numb //= 10
    x += 1

print(f"The number of digits in this number is {x}")
