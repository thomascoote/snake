from turtle import Turtle, Screen
import time
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Snake Game")

def snake_direction():
    pass

segment_list = []
"""Global Options"""

"""Starts the game with a 3 segment snake"""
for i in range (0,4):
    new_snake = Turtle(shape="square")
    new_snake.penup()
    new_snake.pen(fillcolor="white", pencolor="white")
    new_snake.forward(i*20)
    segment_list.append(new_snake)

game_speed = 0.1
is_on = True
while is_on:
    segment_list[len(segment_list)-1].pen(fillcolor="red",pencolor="red")
    screen.update()
    for i in range(0,len(segment_list)-1,1):
        new_x = segment_list[i+1].xcor()
        new_y = segment_list[i+1].ycor()
        segment_list[i].goto(new_x,new_y)
        segment_list[i].pen(pencolor="yellow",fillcolor="yellow")
        screen.update()
    segment_list[len(segment_list)-1].forward(20)
    time.sleep(game_speed)


screen.update()





screen.exitonclick()
