from turtle import Screen
from player import Player
from cars import Cars
from level import Level
import time


screen = Screen()
screen.setup(600, 600)
screen.bgcolor("white")
screen.tracer(0)

player = Player()
car = Cars()
board = Level()
game_is_on = True

screen.listen()
screen.onkey(player.move, "Up")


while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_cars()
    #
    for x in car.all_cars:
        if x.distance(player) < 18:
            game_is_on = False
            board.game_over()
    #
    if player.ycor() > 270:
        player.player_reset()
        car.level_up()
        board.update_scoreboard()
        board.level_update()








screen.exitonclick()