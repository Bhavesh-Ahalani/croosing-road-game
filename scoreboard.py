from turtle import Turtle

FONT = ("Courier", 12, "normal")
GAME_OVER_FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(x=-290, y=280)
        self.update_scoreboard()

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("GAME OVER", align="center", font=GAME_OVER_FONT)
