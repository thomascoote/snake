# main.py

from turtle import Screen
import time
import settings
from snake import Snake
from food import Food
from scoreboard import Scoreboard

def bounds_checker(head, snake, score):
    """Reset if head crosses the screen boundary."""
    max_x = settings.SCREEN_WIDTH / 2
    max_y = settings.SCREEN_HEIGHT / 2
    if not (-max_x < head.xcor() < max_x and -max_y < head.ycor() < max_y):
        score.reset_scoreboard()
        snake.reset()

def main():
    screen = Screen()
    screen.setup(width=settings.SCREEN_WIDTH, height=settings.SCREEN_HEIGHT)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)

    player       = Snake()
    scoreboard   = Scoreboard()
    spawned_food = Food()

    # key bindings
    screen.listen()
    screen.onkeypress(player.up,    "w")
    screen.onkeypress(player.down,  "s")
    screen.onkeypress(player.left,  "a")
    screen.onkeypress(player.right, "d")

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        player.move()

        # wall collision
        bounds_checker(player.head, player, scoreboard)

        # self‑collision
        if player.collision_check():
            scoreboard.reset_scoreboard()
            player.reset()

        # food collision
        if player.head.distance(spawned_food) < settings.SNAKE_SIZE:
            player.extend()
            spawned_food.move_food()
            scoreboard.increase_score()

    screen.exitonclick()

if __name__ == "__main__":
    main()
