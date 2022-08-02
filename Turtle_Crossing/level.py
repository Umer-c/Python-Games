from turtle import Turtle


class Level(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-100, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=("Courier", 24, "normal"))

    def level_update(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=("Courier", 24, "normal"))