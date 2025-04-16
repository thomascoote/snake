from turtle import Turtle
import settings
from settings import SCREEN_HEIGHT, SCREEN_WIDTH, PEN_SETUP

CURRENT_SCORE_POS = ((-(SCREEN_WIDTH/2)) +60, (SCREEN_HEIGHT/2)-40)
HIGH_SCORE_POS = (SCREEN_WIDTH/2) -60, (SCREEN_HEIGHT/2)-40
FONT = ("Arial", 24, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.pen(PEN_SETUP)
        self.penup()
        self.high = 0
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(CURRENT_SCORE_POS)
        self.write(f"Score: {self.score}", align="left", font=FONT)
        self.goto(HIGH_SCORE_POS)
        self.write(f"High score: {self.high}", align="right", font=FONT)

    def increase_score(self):
        self.score += 1
        self.screen.update()
        if self.score > self.high:
            self.high = self.score
        self.update_scoreboard()
