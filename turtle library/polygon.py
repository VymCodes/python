import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(1200,200)
polygon = turtle.Turtle()

num_sides = 57
side_length = 3
angle = 360.0 / num_sides

for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)

turtle.exitonclick() #hi its vyom and i likle turtles