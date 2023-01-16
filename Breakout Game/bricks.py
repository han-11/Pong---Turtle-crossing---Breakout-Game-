from turtle import Turtle
import random

COLORS = ['light blue', 'royal blue',
          'light steel blue', 'steel blue',
          'light cyan', 'light sky blue',
          'violet', 'salmon', 'tomato',
          'sandy brown', 'purple', 'deep pink',
          'medium sea green', 'khaki']


class Brick():

    def __init__(self) -> None:
        self.all_bricks = []
        self.create_all_lanes()

    def create_brick_lane(self, y_cor):
        for i in range(-570, 570, 63):
            new_brick = Turtle('square')
            new_brick.shapesize(stretch_wid=1.5, stretch_len=3)
            new_brick.color(random.choice(COLORS))
            new_brick.penup()
            new_brick.goto(i, y_cor)
            self.all_bricks.append(new_brick)

    def create_all_lanes(self):
        for i in range(0, 240, 32):
            self.create_brick_lane(i)

    def qunatity(self):
        return len(self.all_bricks)
