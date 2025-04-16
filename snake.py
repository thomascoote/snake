from turtle import Turtle, Screen
import time

import settings

SNAKE_SIZE = settings.SNAKE_SIZE
SNAKE_SHAPE = settings.SNAKE_SHAPE
PEN_SETUP = settings.PEN_SETUP

class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.player_segs = [self]
        self.shape(SNAKE_SHAPE)
        self.pen(PEN_SETUP)
        self.penup()
        self.start()

    def start(self):
        #INITIAL SEGMENTS
        for i in range(1,3):
            new_segment = Turtle()
            new_segment.penup()
            new_segment.pen(PEN_SETUP)
            new_segment.shape(SNAKE_SHAPE)
            self.player_segs.append(new_segment)
            new_segment.goto((-20)*i,0)

    def update_snake(self):

        self.player_segs[0].pen(fillcolor="blue")
        self.player_segs[1].pen(fillcolor="yellow")
        self.player_segs[2].pen(fillcolor="pink")

        # Move the body segment to where the segment in front was. Start at index max, head is index 0
        for i in range(len(self.player_segs)-1,0,-1):
            self.player_segs[i].goto(self.player_segs[i-1].xcor(),self.player_segs[i-1].ycor())


    def grow(self):
        new_segment = Turtle()
        new_segment.penup()
        new_segment.pen(fillcolor="black",pencolor="black")
        new_segment.goto(-1000,-1000)
        new_segment.pen(PEN_SETUP)
        new_segment.shape(SNAKE_SHAPE)
        self.player_segs.append(new_segment)

        #Moves the newly added segment to the previous position of the previous index item
        # new_segment.goto(self.player_segs[len(self.player_segs)-1].xcor(),
        #                  self.player_segs[len(self.player_segs)-1].ycor())
