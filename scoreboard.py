from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(0, 380)

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER ', align="center", font=('Courier', 20, 'normal'))

    def increase_score(self):
        self.score += 1

    def display_score(self):
        self.clear()
        self.goto(0, 360)
        self.write(f'SCORE: {self.score}', align="center",  font=('Courier', 20, 'normal'))


