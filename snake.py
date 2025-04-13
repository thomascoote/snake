from turtle import Turtle, Screen
import time

SNAKE_COLOUR = "white"
SNAKE_SIZE = 20
SNAKE_SHAPE = "square"
PEN_SETUP = {
    "pencolor":["white"],
    "fillcolor":["white"],
    "pensize":[20],
}

class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.player_segs = [self]
        self.color(SNAKE_COLOUR)
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
        #Move the first body segment to
        for i in self.player_segs:
            print(f"{i} location = {i.xcor()}")
            time.sleep(0.5)

