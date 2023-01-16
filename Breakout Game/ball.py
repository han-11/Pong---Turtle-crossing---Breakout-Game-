from turtle import Turtle

MOVE_DISTANCE = 10


class Ball(Turtle):

    def _init_(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_move = MOVE_DISTANCE
        self.y_move = MOVE_DISTANCE
        self.reset_position()

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self, x_bounce, y_bounce):
        if x_bounce:
            self.x_move *= -1
        if y_bounce:
            self.y_move *= -1

    def reset_position(self):
        self.goto(0, -240)
        self.y_move = MOVE_DISTANCE
