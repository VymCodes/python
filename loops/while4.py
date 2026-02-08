number = int(input("Enter a number to check for armstong number : "))
number_sum = 0
temp = number
while temp > 0:
    digit = temp % 10
    number_sum = number_sum + (digit ** 3)
    temp = temp//10
if number_sum == number:
    print("this number is an armstrong number")
else:
    print("THIS IS NOT AN ARMSTRONG NUMBER")