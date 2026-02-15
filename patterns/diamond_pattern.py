diamond = int(input("How many rows would you like you diamind to be? : "))
if diamond%2==0:
    half_diamond = int(diamond/2)
else:
    half_diamond = int(diamond/2)+1
space = half_diamond-1
for i in range(1, half_diamond + 1):
    for j in range(1, space+1):
        print(end=" ")
    space = space-1
    num = 1
    for j in range(2*1-1):
        print(end = str(num))
        num = num + 1
    print()
space = 1