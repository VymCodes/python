added = int(input("Enter the number whichs sum you want to find : "))

total_sum = 0

for i in range(1,added + 1):
    total_sum = total_sum + i 
    print(f"The sum of all the numbers till is {i}, so the answer is {total_sum}")

print(f"The sum of all the numbers till {added} is {total_sum}")