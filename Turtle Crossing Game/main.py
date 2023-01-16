import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Create a turtle player that starts at the bottom of the screen and listen for the "Up" keypress to move the turtle north.
player = Player()
cars = CarManager()
scoreboard = Scoreboard()

# Create car objects that are 20px high by 40px wide that randomly generate from the right edge of the screen


# Detect the turtle hit the top edge of the screen, and reset position. palyer level up, car speed increases


# Detect collision with a car, game over and reset level

screen.listen()
screen.onkey(player.go_up, 'Up')


game_is_on = True
while game_is_on:
    cars.create_cars()
    cars.move()
    time.sleep(0.1)
    screen.update()

    # Detect collision with a car
    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect the turtle successfully cross the finish line

    if player.is_at_finish_line():
        player.reset_position()
        cars.level_up()
        scoreboard.increase_level()


screen.exitonclick()
