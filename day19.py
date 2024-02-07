from turtle import  Turtle,Screen
screem= Screen()
t =Turtle()

def move_forward():
    t.forward(20)

screem.listen()
screem.onkey(key="space",fun=move_forward)





















screem.exitonclick()