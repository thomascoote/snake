from random import randrange
from turtle import Turtle, Screen

from snake import Snake, Screen
import time
import random
import keyboard

screen = Screen()

#Initial food
food = Turtle()
spawn_position_x = randrange(-260, 260, 20)
spawn_position_y = randrange(-260, 260, 20)
food.shape("square")
food.pen(fillcolor="blue", pencolor="blue")
food.penup()
food.goto((spawn_position_x,spawn_position_y))

def screen_setup():
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.tracer(0)
    screen.title("Snake Game")
    screen.update()

def check_border(snake_object):
    snake_x_position = snake_object.first_piece().xcor()
    snake_y_position = snake_object.first_piece().ycor()
    if snake_x_position > 260 or snake_y_position > 260 or snake_x_position < -260 or snake_y_position < -260:
        exit()

def spawn_food():
    random_x = randrange(-260,260,20)
    random_y = randrange(-260,260,20)
    food.goto(random_x,random_y)

def check_overlap():
    counter = 0
    segment_positions = []
    for i in new_snake.current_segments():
        counter += 1
        segment_positions.append(i.pos())
        """For debug"""
        # print(segment_positions)
        # print(new_snake.first_piece().pos())
        """"""
    for i in range(0, len(segment_positions)-1):
        if segment_positions[i] == new_snake.first_piece().pos():
            exit()

#Hotkeys
keyboard.add_hotkey('a', lambda: new_snake.turn_left())
keyboard.add_hotkey('d', lambda: new_snake.turn_right())

screen_setup()

new_snake = Snake(screen)


##TODO check if need to grow
##
score = 0
tick_counter = 0
is_on = True
while is_on:
    tick_counter += 1
    new_snake.move()
    check_border(new_snake)
    food_x = int(food.xcor())
    food_y = int(food.ycor())
    first_x = new_snake.first_piece().xcor()
    first_y = new_snake.first_piece().ycor()
    print(f"{food.pos()} --- {new_snake.first_piece().pos()}")
    if tick_counter > 5:
        check_overlap()


    if int(new_snake.first_piece().xcor()) in range(food_x-10,food_x+10) and food.ycor() == int(new_snake.first_piece().ycor()) in range(food_y-10,food_y+10):
        score += 1
        spawn_food()
        print(score)
        new_snake.grow()




screen.exitonclick()
