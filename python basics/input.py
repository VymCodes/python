name = input("Enter your name : ")
print(f"Welcome {name}")

math_score = int(input("Enter score of Math: "))
science_score = int(input("Enter score of Science: "))
literacy_score = int(input("Enter score of Literacy: "))

average = (math_score+science_score+literacy_score)/3

print(f"The average is : {round(average, 1)}")