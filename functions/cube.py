def cubed(number):
    return (number * number * number)


def check(number):
    if number % 3 == 0:
        return cubed(number)
    else:
        return False
    
print(check(5))
print(check(9))
print(check(10))

        