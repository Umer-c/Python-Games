import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=700, height=400)
is_race_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Place your bet on the color: ")

turtle_color = ["red", "lime", "yellow", "black"]
y_position = [0, 50, 100, -50]
all_turtle = []

for i in range(0, 4):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(turtle_color[i])
    tim.goto(-300, y_position[i])
    all_turtle.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        turtle.forward(random.randint(0, 10))
        if turtle.xcor() > 220:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You have won! the {winning_turtle} turtle is the Winner!")
            else:
                print(f"You have lost!, the {winning_turtle} turtle is the Winner!")


# Move turtle with keyboard keys
# def move_forward():
#     tim.forward(10)
#
# def move_backward():
#     tim.back(10)
#
# def move_anitclockwise():
#     tim.setheading(tim.heading() + 10)
#
# def move_clockwise():
#     tim.setheading(tim.heading() - 10)
#
#
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
#
#
# screen.listen()
# screen.onkey(key="d", fun= move_forward)
# screen.onkey(key="a", fun= move_backward)
# screen.onkey(key="s", fun= move_anitclockwise)
# screen.onkey(key="w", fun= move_clockwise)
# screen.onkey(key="c", fun= clear)


screen.exitonclick()