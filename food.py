from turtle import Turtle

import settings
import random

#Food Values
FOOD_SIZE = settings.FOOD_SIZE
FOOD_SHAPE = settings.FOOD_SHAPE
FOOD_SETUP = settings.FOOD_SETUP

#Screen size
SCREEN_X = settings.SCREEN_WIDTH
SCREEN_Y = settings.SCREEN_HEIGHT

class Food(Turtle):
    def __init__(self):
        super().__init__()
        spawn_x = random.randrange(int(-SCREEN_X/2),int(SCREEN_X/2),20)
        spawn_y = random.randrange(int(-SCREEN_Y/2),int(SCREEN_Y/2),20)
        spawn_pos = (spawn_x,spawn_y)
        self.pen(FOOD_SETUP)
        self.shape(FOOD_SHAPE)
        self.color("red")
        self.penup()
        self.goto(spawn_pos)

    def move_food(self):
        move_x = random.randrange(int(-SCREEN_X / 2), int(SCREEN_X / 2), 20)
        move_y = random.randrange(int(-SCREEN_Y / 2), int(SCREEN_Y / 2), 20)
        move_pos = (move_x,move_y)
        self.goto(move_pos)