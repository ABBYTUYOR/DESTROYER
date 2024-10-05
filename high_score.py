from turtle import Turtle

class High_score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('white')

    def display_high_score(self, score):
        self.goto(340, 360)
        self.write(f'HIGH SCORE: {score}', align="center", font=('Courier', 20, 'normal'))
