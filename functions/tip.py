def total_bill(bill_amount,tip_percent):
    return bill_amount + (bill_amount * (tip_percent / 100))
bill_amount = int(input("Enter the amount of the bill : "))
tip_percent = int(input("Enter the tip you want to give : "))
print(total_bill(bill_amount,tip_percent))

