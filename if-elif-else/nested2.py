units = float(input("How many electricity units have been used "))
if units < 50:
    amount = units * 2.60
    tax = 0 
elif units < 100:
    amount = units * 3
    tax = 20
elif units < 150:
    amount = units * 3.5
    tax = 30

elif units < 250:
    amount = units * 4.5
    tax = 50
else:
    amount = units * 4
    tax = 40

total_bill = amount+tax

print(f"Your total bill is ${total_bill} ")