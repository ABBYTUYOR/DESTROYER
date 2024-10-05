import turtle
from turtle import Turtle

class Starship(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-400, 0)
        turtle.register_shape('starship.gif')
        self.shape('starship.gif')



    def move_up(self):
        new_y = self.ycor() + 30
        self.goto(self.xcor(),new_y)

    def move_down(self):
        new_y = self.ycor() - 30
        self.goto(self.xcor(),new_y)


    def move_right(self):
        new_x = self.xcor() + 50
        self.goto(new_x, self.ycor())

    def move_left(self):
        new_x = self.xcor() - 50
        self.goto(new_x, self.ycor())

