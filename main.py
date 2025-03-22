from turtle import Turtle, Screen
import time
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Snake Game")

snake_list = []
"""Global Options"""

"""Starts the game with a 3 segment snake"""
for i in range (0,4):
    new_snake = Turtle(shape="square")
    new_snake.penup()
    new_snake.pen(fillcolor="white", pencolor="white")
    new_snake.forward(i*20)
    snake_list.append(new_snake)

game_speed = 0.1
is_on = True
while is_on:
    screen.update()
    for i in snake_list:
        i.forward(20)
        time.sleep(game_speed)

screen.update()





screen.exitonclick()
