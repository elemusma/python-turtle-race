from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

tim.forward(10)
tim.degrees(400.0)


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def move_clockwise():
    tim.right(45)


def move_counter_clockwise():
    tim.left(45)


def clear():
    tim.clear()
    tim.penup()
    tim.setx(0)
    tim.sety(0)
    tim.setheading(0)
    tim.pendown()



screen.listen()
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='s', fun=move_backward)
screen.onkey(key='d', fun=move_clockwise)
screen.onkey(key='a', fun=move_counter_clockwise)
screen.onkey(key='c', fun=clear)
screen.exitonclick()