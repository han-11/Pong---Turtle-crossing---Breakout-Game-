from turtle import Turtle, Screen
from paddle_breakout import Paddle
from ball import Ball
from bricks import Brick
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=1200, height=600)
screen.bgcolor('black')
screen.title('Breakout Game')
screen.tracer(0)


# Create the paddle object
paddle = Paddle()

# Create the ball object
ball = Ball()

# Create the brick object
bricks = Brick()

# Create the scoreboard object
scoreboard = Scoreboard()


screen.listen()
screen.onkey(paddle.move_left, 'Left')
screen.onkey(paddle.move_right, 'Right')

# Detect collision with walls


def check_wall_collision():
    global ball, scoreboard

# Detet collision with left and right walls
    if ball.xcor() > 580 or ball.xcor() < -580:
        ball.bounce(True, False)

# Detect collision with top wall
    if ball.ycor() > 280:
        ball.bounce(False, True)
# Detect collision with bottom wall, game over

    if ball.ycor() < -280:
        ball.reset_position()
        scoreboard.game_over()

# Detect collision with paddle


def check_collision_with_paddle():
    global ball, paddle

    if ball.distance(paddle) < 110 and ball.ycor() < -250:

        # If paddle on the right screen
        if paddle.xcor() > 0:
            # IF BALL HITS ON THE RIGHT SIDE OF THE PADDLE
            if ball.xcor() > paddle.xcor():
                ball.bounce(True, True)
            else:
                ball.bounce(False, True)

        # If paddle on the left screen
        if paddle.xcor() < 0:
            # IF BALL HITS ON THE LEFT SIDE OF THE PADDLE
            if ball.xcor() < paddle.xcor():
                ball.bounce(True, True)
            else:
                ball.bounce(False, True)

        else:
            if ball.xcor() < paddle.xcor():
                ball.bounce(True, True)
            elif ball.xcor() > paddle.xcor():
                ball.bounce(True, True)
            else:
                ball.bounce(False, True)


# Detect collision with bricks
def check_collision_with_bricks():
    global ball, bricks, scoreboard

    for brick in bricks.all_bricks:
        if ball.distance(brick) < 40:
            scoreboard.increase_score()
            bricks.qunatity -= 1

            # Detect collision with left and right walls


# Main game loop
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()
    check_wall_collision()
    check_collision_with_paddle()
    check_collision_with_bricks()

    if bricks.qunatity == 0:
        bricks.reset_bricks()
        ball.reset_position()
        scoreboard.win()
        break


screen.exitonclick()
