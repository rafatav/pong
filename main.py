from turtle import Turtle, Screen
from stick import Stick
from ball import Ball
from wall import Wall
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=1280, height=720)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

stick = Stick()
wall = Wall()
ball = Ball()
score = Scoreboard()

screen.onkeypress(fun=stick.move_1_up, key="w")
screen.onkeypress(fun=stick.move_1_down, key="s")
screen.onkeypress(fun=stick.move_2_up, key="Up")
screen.onkeypress(fun=stick.move_2_down, key="Down")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0)
    ball.move_ball()
    for block in wall.side_wall_list:
        if ball.distance(block.position()) < 15:
            ball.reset_ball()
            ball = Ball()
            if block.xcor() > 600:
                score.scoreboard_1()
            else:
                score.scoreboard_2()
    for block in wall.wall_list:
        if ball.distance(block.position()) < 15:
            ball.bounce_wall()
    for block in stick.stick_1:
        if ball.distance(block.position()) < 15:
            ball.bounce_stick()
    for block in stick.stick_2:
        if ball.distance(block.position()) < 15:
            ball.bounce_stick()

