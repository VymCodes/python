pay = float(input("How much would you like to pay : "))
bill = 50
due = bill-pay
extra = pay-bill

if pay < bill:
    print(f"You are ${due} short because the bill was $50")
elif pay > bill:
    print(f"You paid extra by {extra} becuase the bill was $50")
else:
    print("You bill of $50 is paid!")

