# the mean of 40 numbers is 38. later on, I detected that i missread the number as 56 as 36

How_many_numbers = 40

Incorrect_mean = 38

Missread_number = 36

Real_number = 56

Diffrence_in_the_missread_number_and_the_real_one = (Real_number - Missread_number)

Incorrect_Sum_of_all_the_numbers = (How_many_numbers * Incorrect_mean)

Corrected_Sum_of_all_the_numbers = (Incorrect_Sum_of_all_the_numbers + Diffrence_in_the_missread_number_and_the_real_one)

Corrected_mean = (Corrected_Sum_of_all_the_numbers / How_many_numbers)

print(f"The correct anwser is {Corrected_mean}")