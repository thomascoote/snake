from random import randrange
from turtle import Turtle, Screen
import time
import snake

UP = (0,20)
DOWN = (0,-20)
LEFT = (-20,0)
RIGHT = (20,0)


screen = Screen()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")

def move_right():
    screen.tracer(0)
    player.setheading(0)
    screen.tracer(1)

def move_left():
    screen.tracer(0)
    player.setheading(180)
    screen.tracer(1)

def move_up():
    screen.tracer(0)
    player.setheading(90)
    screen.tracer(1)

def move_down():
    screen.tracer(0)
    player.setheading(270)
    screen.tracer(1)

#Make the starting snake
player = snake.Snake()
print("Player initialised")

screen.onkeypress(fun=move_up, key="w")
screen.onkeypress(fun=move_left, key="a")
screen.onkeypress(fun=move_down, key="s")
screen.onkeypress(fun=move_right, key="d")


screen.listen()

is_on = True
while is_on:
    player.forward(20)
    player.update_snake()
    time.sleep(0.1)

screen.exitonclick()
