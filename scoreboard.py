from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_2 = 0
        self.score_1 = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-300, 200)
        self.write(f"{self.score_1}", font=('Arial', 60, 'normal'))
        self.goto(300, 200)
        self.write(f"{self.score_2}", font=('Arial', 60, 'normal'))

    def scoreboard_1(self):
        self.clear()
        self.score_1 += 1
        self.update_scoreboard()

    def scoreboard_2(self):
        self.clear()
        self.score_2 += 1
        self.update_scoreboard()

