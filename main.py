from random import randrange
from turtle import Turtle, Screen
from scoreboard import Scoreboard
from snake import Snake, Screen
import time
import random
import keyboard

#TODO - High Score module

screen = Screen()

#Initial food
food = Turtle()
spawn_position_x = randrange(-260, 260, 20)
spawn_position_y = randrange(-260, 260, 20)
food.shape("square")
food.pen(fillcolor="blue", pencolor="blue")
food.penup()
food.goto((spawn_position_x,spawn_position_y))

score = Scoreboard()

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

def check_eat():
    new_snake_x = round(new_snake.first_piece().pos()[0],2)
    new_snake_y = round(new_snake.first_piece().pos()[1],2)
    snake_head_pos = (new_snake_x,new_snake_y)
    food_x = food.pos()[0]
    food_y = food.pos()[1]

    # print(f"{new_snake_x},{new_snake_y},{food_x},{food_y}")
    if snake_head_pos == food.pos():
        new_snake.grow()
        spawn_food()
        score.increase_score()
    else:
        pass

def check_overlap():
    segment_positions = []
    for i in new_snake.current_segments():
        segment_positions.append(i.pos())

    for i in range(1, len(segment_positions)):  # Start from 1 to exclude the head.
        if segment_positions[i] == new_snake.first_piece().pos():
            print(f"Collision detected: {segment_positions[i]} equals head at {new_snake.first_piece().pos()}")


#Hotkeys
keyboard.add_hotkey('a', lambda: new_snake.turn_left())
keyboard.add_hotkey('d', lambda: new_snake.turn_right())

screen_setup()
new_snake = Snake()

tick_counter = 0
is_on = True
while is_on:
    tick_counter += 1
    new_snake.move()
    check_eat()
    check_border(new_snake)

    if tick_counter > 5:
        check_overlap()

    if tick_counter == 20:
        for i in new_snake.segment_list:
            i.clear()
        new_snake = Snake()
exit()
screen.exitonclick()
