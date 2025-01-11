from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 50


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color('white')
        self.shapesize(stretch_len=5)
        self.goto(STARTING_POSITION)

    def move_right(self):
        self.forward(MOVE_DISTANCE)

    def move_left(self):
        self.backward(MOVE_DISTANCE)
