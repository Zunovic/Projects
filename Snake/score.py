from turtle import Turtle

with open("save_game.txt") as file:
    saved_score = file.read()

ALIGNMENT = "center"
FONT = ("Courier", 22, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = int(saved_score)
        self.hideturtle()
        self.color("white")
        self.up()
        self.goto(0, 265)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} Highest: {self.highscore}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset_score(self):
        if self.score > self.highscore:
            with open("save_game.txt", mode="w") as fil:
                fil.write(str(self.score))
            self.highscore = self.score
        self.score = 0
        self.update_score()

