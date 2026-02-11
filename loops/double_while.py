wrd = input("Enter a word : ")
char = input("Enter a charecter to find : ")
i = 0
count = 0

while i < len(wrd):
    if wrd[i]== char:
        count = count + 1
    i = i + 1

print(count)