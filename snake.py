from turtle import Turtle, Screen
import time
import keyboard

class Snake:

    def __init__(self, screen):
        self.turtle = Turtle()
        self.colour = "white"
        self.shape ="square"
        self.initial_segments()
        self.screen = screen

    def first_piece(self):
        return self.segment_list[len(self.segment_list) - 1]

    def initial_segments(self):
        self.segment_list = []

        for i in range(0, 4):
            new_snake = Turtle(shape="square")
            new_snake.penup()
            new_snake.pen(fillcolor="white", pencolor="white")
            new_snake.goto(-i * 20, 0)
            self.segment_list.append(new_snake)

    def move(self):
        segment_list = self.segment_list
        first_segment = self.first_piece()
        first_segment.pen(fillcolor="white", pencolor="white")
        self.screen.update()
        for i in range(0, len(segment_list) - 1, 1):
            new_x = segment_list[i + 1].xcor()
            new_y = segment_list[i + 1].ycor()
            segment_list[i].goto(new_x, new_y)
            segment_list[i].pen(pencolor="white", fillcolor="white")
        first_segment.forward(20)
        self.screen.update()
        time.sleep(0.3)

    # def grow(self):
    #     last_piece = self.segment_list[len(self.segment_list)-1]
    #     piece_x = last_piece.xcor()
    #     piece_y = last_piece.ycor()
    #     piece_dir = last_piece.heading()
    #     #New piece to be added
    #     new_piece = Turtle(shape="square")
    #     new_piece.xcor =



    def turn_left(self):
        segment_list = self.segment_list
        first_segment = segment_list[len(segment_list) - 1]
        first_segment.left(90)
    def turn_right(self):
        segment_list = self.segment_list
        first_segment = segment_list[len(segment_list) - 1]
        first_segment.right(90)