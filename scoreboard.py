from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.keep_score()
        self.car_counter = 6

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", font=FONT)

    def keep_score(self):
        self.clear()
        self.goto(-280, 260)
        self.write(f"Level: {self.level}", font=FONT)
        if self.level == 3 or self.level == 5:
            self.car_counter -= 1
