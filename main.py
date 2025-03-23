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
    # print(food.pos())

    # return food

#Hotkeys
keyboard.add_hotkey('a', lambda: new_snake.turn_left())
keyboard.add_hotkey('d', lambda: new_snake.turn_right())

screen_setup()

new_snake = Snake(screen)


##TODO check if need to grow
##


score = 0
is_on = True
while is_on:
    new_snake.move()
    check_border(new_snake)
    new_snake.grow()

    # print(food.pos())
    # print(new_snake.first_piece().pos())

    # if food.xcor() == new_snake.first_piece().xcor() and food.ycor() == new_snake.first_piece().ycor():
    #     score += 1
    #     spawn_food()
    #     print(score)




screen.exitonclick()
