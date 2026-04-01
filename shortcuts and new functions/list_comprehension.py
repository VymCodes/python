#The code with the 4 lines and the one with 1 line does the same thing
sqr_numbers = []
for i in range(20):
    sqr_numbers.append(i*i)

print(sqr_numbers)


cool_sqr = [i*i for i in range(20)] #fit many lines into 1
print(cool_sqr)

