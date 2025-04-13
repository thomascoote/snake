from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.high = 0
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:{self.score}", align="center", font=("Arial", 24, "normal"))
        self.goto(200,260)
        self.write(f"High score:{self.high}", align="center", font=("Arial", 24, "normal"))
        self.goto(0,260)

    def increase_score(self):
        self.score += 1
        self.screen.update()
        if self.score >= self.high:
            self.high = self.score
        self.update_scoreboard()
