from turtle import Turtle

MOVE_DISTANCE = 70


class Paddle(Turtle):
    def _init_(self):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=10)
        self.color('white')
        self.penup()
        self.goto(0, -280)

    def move_left(self):
        self.backward(MOVE_DISTANCE)

    def move_right(self):
        self.forward(MOVE_DISTANCE)
