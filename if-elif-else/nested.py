Yes_or_no = (input("Do you have a medical cause? Yes/No : "))
attendence = int(input("What is your attendence "))
if Yes_or_no == "yes" or "YES":
    print("You can take the test")
else:
    if attendence >= 75:
        print("you can take the test")
    else:
        print("you can not take the test")
