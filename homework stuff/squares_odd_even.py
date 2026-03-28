beggining = int(input("What is the beggining of the range : "))
finish = int(input("What is the end of the range : "))

odd_squares = []
even_squares = []


for number in range(beggining, finish):
    square = number ** 2
    
    if square % 2 == 0:
        even_squares.append(square)
    else:
        odd_squares.append(square)
        
print(f"The even squares are {even_squares}")
print(f"The odd squares are {odd_squares}")