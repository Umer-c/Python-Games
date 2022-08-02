from turtle import Turtle

class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.tilt(90)
        self.penup()
        self.color("lime")
        self.goto(0, -270)


    def move(self):
        new_y = self.ycor() + 20
        self.goto(0, new_y)

    def player_reset(self):
        self.goto(0, -270)