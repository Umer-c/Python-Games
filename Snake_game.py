import random
from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
score = 0
score_board = Turtle()
score_board.penup()
score_board.hideturtle()
score_board.color("white")
score_board.goto(0, 260)
score_board.write(f"Score: {score}", align="center", font=("Arial", 24, "normal"))
score_board.speed("fastest")


x_pos = 0
all_turtle = []
screen.tracer(0)

turtle_length = 3

#Create snake
for i in range(0, turtle_length):
    turtle = Turtle(shape="square")
    turtle.color("white")
    turtle.penup()
    turtle.goto(x_pos, 0)
    all_turtle.append(turtle)
    x_pos += 20

game_is_on = True

head = all_turtle[0]

#move snake
def up():
    if head.heading() != 270:
        head.setheading(90)
def down():
    if head.heading() != 90:
        head.setheading(270)

def left():
    if head.heading() != 0:
        head.setheading(180)

def right():
    if head.heading() != 180:
        head.setheading(0)

screen.listen()
screen.onkey(key="Up", fun=up)
screen.onkey(key="Down", fun=down)
screen.onkey(key="Left", fun=left)
screen.onkey(key="Right", fun=right)


#creating food
food = Turtle(shape="circle")
food.shapesize(0.5, 0.5)
food.penup()
food.color("red")
food.speed("fastest")
food.goto(random.randint(-280, 280), random.randint(-280, 280))


print(all_turtle[0].distance(all_turtle[1]))

#To move the snake
while game_is_on:
    screen.update()
    time.sleep(0.1)

    #to move snake forward, we need to link them
    for turtle_num in range(len(all_turtle) - 1, 0, -1): #2, 0, -1
        #I need to move turtle 3 on position of turtle 2, So we need position cords of turtle 2
        new_x = all_turtle[turtle_num - 1].xcor()
        new_y = all_turtle[turtle_num - 1].ycor()
        all_turtle[turtle_num].goto(new_x, new_y)
    all_turtle[0].forward(20)

    # detect collision food
    if head.distance(food) < 15:
        food.goto(random.randint(-270, 270), random.randint(-270, 270))
        score += 1
        score_board.clear()
        score_board.write(f"Score: {score}", align="center", font=("Arial", 24, "normal"))
        new_turtle = Turtle(shape="square")
        new_turtle.penup()

        all_turtle.append(new_turtle)
        new_turtle.color("white")


    #detect collision with wall
    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
        game_is_on = False
        score_board.goto(0,0)
        score_board.write("Game Over", align="center", font=("Arial", 24, "normal"))

    # detect collision with body
    # for seg in all_turtle[1:]:
    #     if head.distance(seg) < 20:
    #         game_is_on = False
    #         score_board.goto(0, 0)
    #         score_board.write("Game Over", align="center", font=("Arial", 24, "normal"))




screen.exitonclick()