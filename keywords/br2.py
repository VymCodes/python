name = (input("What is your name : "))
i = -1
for char in name:
    i = i + 1
    if char == "a":
        print("FOUND YOU HAHAHAH")
        print(char)
        print(f"The index is {i}")
        break