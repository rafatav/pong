from turtle import Turtle
import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.goto(x=0, y=random.randint(-270, 270))
        self.setheading(random.choice([135, -135, 45, -45]))

    def move_ball(self):
        self.heading()
        self.forward(8)

    def reset_ball(self):
        self.reset()

    def bounce_wall(self):
        if self.heading() > 90:
            new_heading = 270 - (self.heading() - 90)
            self.setheading(new_heading)
        elif self.heading() > 180:
            new_heading = 360 - (self.heading() - 180)
            self.setheading(new_heading)
        elif self.heading() > 270:
            new_heading = 90 - (self.heading() - 270)
            self.setheading(new_heading)
        else:
            new_heading = 270 + self.heading()
            self.setheading(new_heading)

    def bounce_stick(self):
        if self.heading() > 90:
            new_heading = 90 - (self.heading() - 90)
            self.setheading(new_heading)
        elif self.heading() > 180:
            new_heading = 180 - (self.heading() - 180)
            self.setheading(new_heading)
        elif self.heading() > 270:
            new_heading = 270 - (self.heading() - 270)
            self.setheading(new_heading)
        else:
            new_heading = 90 + self.heading()
            self.setheading(new_heading)
