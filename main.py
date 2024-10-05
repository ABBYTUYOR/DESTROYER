import time
from time import sleep
from turtle import Screen
from asteroid import Asteroid
from starship import Starship
from weapon import Weapon
from scoreboard import Scoreboard
from high_score import High_score


screen = Screen()
screen.setup(width=1000, height=800)
screen.title("ASTEROID DESTROYER 🚀")
screen.bgpic("space.png")
screen.tracer(0)

ship = Starship()
weapon = Weapon()
asteroid = Asteroid()
scoreboard = Scoreboard()
scoreboard.display_score()
high_score = High_score()

with open("score.txt") as file:
    content = file.read()

high_score.display_high_score(content)

screen.listen()
screen.onkey(ship.move_up, 'w')
screen.onkey(ship.move_down, 's')
screen.onkey(ship.move_right, 'd')
screen.onkey(ship.move_left, 'a')

game_is_on = True

while game_is_on:
    screen.update()
    sleep(0.1)
    asteroid.create_asteroid()
    asteroid.moving_asteroid()
    weapon.create_fire(ship.xcor(), ship.ycor())
    weapon.on_fire()

    for collide in asteroid.asteroids:
        if collide.distance(ship) < 40:
            scoreboard.game_over()
            game_is_on = False
            if int(scoreboard.score) > int(content):
                final_score = scoreboard.score
                print(final_score)
                with open("score.txt", mode="w") as File:
                    File.write(str(final_score))
    for fire in weapon.weapons:

        for asteroid_x in asteroid.asteroids:
            if fire.distance(asteroid_x) < 20:
                asteroid_x.teleport(1000,1000)
                scoreboard.increase_score()
                scoreboard.display_score()



    if ship.ycor() > 380:
        ship.goto(ship.xcor(), 380)

    if ship.ycor() < -380:
        ship.goto(ship.xcor(), -380)

    if ship.xcor() > 450:
        ship.goto(450, ship.ycor())

    if ship.xcor() < -450:
        ship.goto(-450, ship.ycor())


screen.exitonclick()