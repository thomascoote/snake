# snake.py

from turtle import Turtle
import settings

STARTING_POSITIONS = [
    (0, 0),
    (-settings.SNAKE_SIZE, 0),
    (-settings.SNAKE_SIZE * 2, 0)
]
MOVE_DISTANCE = settings.SNAKE_SIZE
SNAKE_SHAPE   = settings.SNAKE_SHAPE
PEN_SETUP     = settings.PEN_SETUP

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Build the head + two body segments."""
        for pos in STARTING_POSITIONS:
            self.add_segment(pos)

    def add_segment(self, position):
        """Create one segment at `position`."""
        seg = Turtle()
        seg.shape(SNAKE_SHAPE)
        seg.penup()
        seg.pen(**PEN_SETUP)
        seg.goto(position)
        self.segments.append(seg)

    def extend(self):
        """Add a segment at the tail’s current position."""
        tail_pos = self.segments[-1].position()
        self.add_segment(tail_pos)

    def move(self):
        """Move each segment to the spot vacated by the one in front."""
        for idx in range(len(self.segments) - 1, 0, -1):
            x = self.segments[idx - 1].xcor()
            y = self.segments[idx - 1].ycor()
            self.segments[idx].goto(x, y)
        self.head.forward(MOVE_DISTANCE)

    # direction controls — prevents 180° turns
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def collision_check(self):
        """Return True if head collides with any *extra* segment."""
        for seg in self.segments[3:]:
            if self.head.distance(seg) < settings.SNAKE_SIZE:
                return True
        return False

    def reset(self):
        """Hide all old segments and rebuild the 3‑segment snake."""
        for seg in self.segments:
            seg.hideturtle()
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        self.head.setheading(0)
