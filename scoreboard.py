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
        self.penup()
        with open("high_score.txt", mode="r") as data_in:
            self.high = int(data_in.read())
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(CURRENT_SCORE_POS)
        self.write(f"Score: {self.score}", align="left", font=FONT)
        self.goto(HIGH_SCORE_POS)
        self.write(f"High score: {self.high}", align="right", font=FONT)

    def increase_score(self):
        self.write_over_black()
        self.score += 1
        if self.score > self.high:
            self.high = self.score
            with open("high_score.txt",mode="w") as data:
                data.write(str(self.high))
        self.update_scoreboard()

    def reset_scoreboard(self):
        self.write_over_black()
        self.score = 0
        print(self.score)
        self.update_scoreboard()

    def write_over_black(self):
        #Write over previous text with black
        self.screen.tracer(0)
        self.pen(pensize=100,pencolor="black",fillcolor="black")
        self.shape("square")
        self.goto(CURRENT_SCORE_POS)
        self.pendown()
        self.goto(HIGH_SCORE_POS)
        self.penup()
        #Set pen back to writing mode
        self.pen(PEN_SETUP)