from shlex import shlex
from turtle import Turtle
from starship import Starship


class Weapon:
    def __init__(self):
        self.weapons = []

    def create_fire(self, ship_x, ship_y):
        fire = Turtle()
        fire.penup()
        fire.shape("square")
        fire.shapesize(stretch_len=0.5,stretch_wid=0.5)
        fire.color("yellow")
        fire.speed("fastest")
        fire.forward(10)
        fire.goto(ship_x, ship_y)
        self.weapons.append(fire)

    def on_fire(self):
        for fire in self.weapons:
            fire.forward(30)



