from random import randrange
from turtle import Turtle, Screen
import time

import scoreboard
import snake
import settings
import food
from scoreboard import Scoreboard

screen = Screen()
score = Scoreboard()

SCREEN_WIDTH = settings.SCREEN_WIDTH
SCREEN_HEIGHT = settings.SCREEN_HEIGHT

screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
def bounds_checker():
    if (SCREEN_WIDTH/2) < player.xcor() > (SCREEN_WIDTH/2) or (SCREEN_HEIGHT/2) < player.ycor() > (SCREEN_HEIGHT/2):
        exit()

def grow():
    player.grow()

#IF statement prevents snake from reversing course

def move_right():
    if player.heading() != 180:
        screen.tracer(0)
        player.setheading(0)
        screen.tracer(1)

def move_left():
    if player.heading() != 0:
        screen.tracer(0)
        player.setheading(180)
        screen.tracer(1)

def move_up():
    if player.heading() != 270:
        screen.tracer(0)
        player.setheading(90)
        screen.tracer(1)

def move_down():
    if player.heading() != 90:
        screen.tracer(0)
        player.setheading(270)
        screen.tracer(1)

def forward():
    player.forward(20)

#Make the starting snake
player = snake.Snake()

#Initialise the scoreboard
screen.tracer(0)
scoreboard.Scoreboard()
screen.tracer(1)

screen.onkeypress(fun=move_up, key="w")
screen.onkeypress(fun=move_left, key="a")
screen.onkeypress(fun=move_down, key="s")
screen.onkeypress(fun=move_right, key="d")

screen.listen()

#Spawn the food
screen.tracer(0)
spawned_food = food.Food()
screen.tracer(1)

print(spawned_food.pos())
is_on = True
while is_on:

    #Disable screen update while moving the snake segments into their new position
    screen.tracer(0)
    player.update_snake()
    screen.ontimer(fun=forward(), t=100)

    #Reenable screen update after all segments in their new position.
    screen.tracer(1)

    #Check if head has eaten some food
    if player.distance(spawned_food) < 5:
        screen.tracer(0)
        player.grow()
        spawned_food.move_food()
        score.increase_score()
        screen.tracer(1)

    #Checks if player hits the wall
    bounds_checker()

screen.exitonclick()
