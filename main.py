import random

print("welcome to python graphics")
from turtle import Turtle, Screen

timmy_the_turtle = Turtle()




timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.clone()
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(200)
# timmy_the_turtle.left(45)
# timmy_the_turtle.forward(899)



# for _ in   range(15):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()

# def draw_shape(num_side):
#     angel = 360/num_side
#     for _ in range(num_side):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(angel)
#
# for shape in range(3,11):
#     draw_shape(shape)












directin = [0,90,180,270]

for _ in range(200):
    timmy_the_turtle.forward(30)
    timmy_the_turtle.setheading(random.choice(directin))

random.c
















screen = Screen()
screen.exitonclick()