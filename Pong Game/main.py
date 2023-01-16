from turtle import Turtle, Screen
import time
from paddleobject import Paddle
from ball import Ball
from scoreboard import Scoreboard


# Create the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

# Create and move a paddle

pad_r = Paddle((350, 0))
pad_l = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# make the screen listen to keypress
screen.listen()
screen.onkey(pad_r.go_up, "Up")
screen.onkey(pad_r.go_down, "Down")
screen.onkey(pad_l.go_up, "w")
screen.onkey(pad_l.go_down, "s")


# Keep score

game_is_on = True
while game_is_on:
  # make the ball move animation speed slow
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(pad_r) < 50 and ball.xcor() > 320 or ball.distance(pad_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()

   # Detect when right paddle misses
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset_position()

    # Detect when left paddle misses
    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset_position()


screen.exitonclick()
