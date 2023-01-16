from turtle import Turtle

try:
    score = open('score.txt', 'r').read()
except FileNotFoundError:
    score = open('score.txt', 'w').write(str(0))
except ValueError:
    score = 0


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(-580, 270)
        self.high_score = int(score)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score}', align='center',
                   font=('Courier', 24, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        if self.score > self.high_score:
            self.high_score = self.score
            open('score.txt', 'w').write(str(self.high_score))
        self.update_scoreboard()

    def win(self):
        self.clear()
        self.write('YOU CLEARED THE GAME', align='center',
                   font=('Courier', 24, 'normal'))
        open('score.txt', 'w').write(str(self.high_score))

    def game_over(self):
        self.clear()
        self.score = 0
        self.update_scoreboard()
        self.write('GAME OVER', align='center', font=('Courier', 24, 'normal'))
        open('score.txt', 'w').write(str(self.high_score))
