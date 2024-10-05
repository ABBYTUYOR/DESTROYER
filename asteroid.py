import turtle
from turtle import Turtle, register_shape
import random


class Asteroid:
    def __init__(self):
        self.asteroids = []

    def create_asteroid(self):
        random_chance = random.randint(1, 15)
        if random_chance == 1:
            asteroid = Turtle()
            asteroid.penup()
            turtle.register_shape('a1.gif')
            asteroid.shape("a1.gif")
            asteroid.shapesize(stretch_len=0.5, stretch_wid=0.5)
            asteroid.color("yellow")
            asteroid.speed("fastest")
            random_y = random.randint(-370, 370)
            asteroid.goto(400, random_y)
            asteroid.setheading(180)
            self.asteroids.append(asteroid)

    def moving_asteroid(self):
        for obs in self.asteroids:
            obs.forward(20)

    def hit_asteroid(self, x):
            self.asteroids.remove(self.asteroids[0])


