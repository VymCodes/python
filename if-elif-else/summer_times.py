weather = int(input( " How many degrees celcius is it today? : "))
if weather <= 10:
    print("You have to wear a jacket")
elif weather <= 20:
    print("You can wear light clothes")
else:
    print("Yay! Summer time!")