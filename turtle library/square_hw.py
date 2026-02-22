import turtle


turtle.Screen().bgcolor("blue")
turtle.Screen().setup(666200,6666200)
square = turtle.Turtle()

num_sides = 4
side_length = 88
angle = 360.0 / num_sides

for i in range(num_sides):
    square.forward(side_length)
    square.right(angle)

turtle.exitonclick() #hi its vyom and i likle turtles