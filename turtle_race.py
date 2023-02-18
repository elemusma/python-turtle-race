from turtle import Turtle, Screen
from random_color import RandomTuple
import random

screen = Screen()
screen.setup(width=500, height=400)

is_race_on = False
colors = ['red', 'orange', 'purple', 'brown', 'green', 'blue', 'magenta']
user_input = screen.textinput("What's your bet?", "Who do you think will win?")
turtles = []

def create_turtles(num_of_turtles):
    # i = 0
    current_y = -125
    current_x = -240
    for turtle_index in range(num_of_turtles):
        new_turtle = Turtle(shape="turtle")
        new_turtle.penup()
        new_turtle.color(colors[turtle_index])
        new_turtle.goto(x=current_x,y=current_y)
        turtles.append(new_turtle)

        current_y = current_y + 50


create_turtles(6)
print(turtles)

if user_input:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        rand_distance = random.randrange(0,10)
        turtle.forward(rand_distance)
        if turtle.xcor() > 230:
            if turtle.color()[0] == user_input:
                print("Congrats! You've won")
            else:
                print(f"You bet on the wrong turtle. The winner is {turtle.color()[0]}.")
            is_race_on = False
        # print(turtle)
        # print(user_input)


# print(user_input)


# tim1.penup()
# tim1.goto(x=-240, y=0)


screen.exitonclick()