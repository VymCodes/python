number = int(input("enter a number to find the sum till :"))
current_total = 0

while number > 0:
    current_total = current_total + number 
    number -= 1
    

print(f"The sum is {current_total}")