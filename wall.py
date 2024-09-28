from turtle import Turtle

SCREEN_WIDTH = 1230
SCREEN_HEIGHT = 720


class Wall(Turtle):


    def __init__(self):
        super().__init__()
        self.wall_list = []
        self.side_wall_list = []
        self.ceiling_wall()
        self.floor_wall()
        self.right_side_wall()
        self.left_side_wall()

    def create_wall(self, wid, ht):
        block_wall = Turtle(shape="square")
        block_wall.color("black")
        block_wall.penup()
        block_wall.goto(x=wid, y=ht)
        if ht == 368 or ht == -361:
            self.wall_list.append(block_wall)
        else:
            self.side_wall_list.append(block_wall)

    def ceiling_wall(self):
        wid = -630
        ht = 368
        for ceiling_block in range(int(SCREEN_WIDTH / 20)+3):
            self.create_wall(wid, ht)
            wid += 20

    def floor_wall(self):
        wid = -630
        ht = -361
        for floor_block in range(int(SCREEN_WIDTH / 20)+3):
            self.create_wall(wid, ht)
            wid += 20

    def right_side_wall(self):
        wid = 640
        ht = 400
        for side_block in range(int(SCREEN_HEIGHT / 20)+5):
            self.create_wall(wid, ht)
            ht += -20

    def left_side_wall(self):
        wid = -648
        ht = 400
        for side_block in range(int(SCREEN_HEIGHT / 20)+5):
            self.create_wall(wid, ht)
            ht += -20