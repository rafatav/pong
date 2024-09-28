from turtle import Turtle

INITIAL_1 = [(-590, 0), (-590, 20), (-590, -20), (-590, -40)]
INITIAL_2 = [(590, 0), (590, 20), (590, -20), (590, -40)]


class Stick(Turtle):

    def __init__(self):
        super().__init__()
        self.stick_1 = []
        self.stick_2 = []
        self.create_stick_1()
        self.create_stick_2()

    def create_stick(self, position, lists):
        for blk in range(len(position)):
            stick_block = Turtle(shape="square")
            stick_block.color("white")
            stick_block.penup()
            stick_block.goto(position[blk])
            lists.append(stick_block)

    def create_stick_1(self):
        self.create_stick(INITIAL_1, self.stick_1)

    def create_stick_2(self):
        self.create_stick(INITIAL_2, self.stick_2)

    def move_1_up(self):
        for block in self.stick_1:
            block.setheading(90)
            block.forward(30)

    def move_1_down(self):
        for block in self.stick_1:
            block.setheading(270)
            block.forward(30)

    def move_2_up(self):
        for block in self.stick_2:
            block.setheading(90)
            block.forward(30)

    def move_2_down(self):
        for block in self.stick_2:
            block.setheading(270)
            block.forward(30)
