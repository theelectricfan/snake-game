import turtle


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("data.txt", mode="r") as data:
            self.highscore = int(data.read())
        self.hideturtle()
        self.penup()
        self.goto(0,250)
        self.color("aqua")
        self.write(f"Score = {self.score} Highscore = {self.highscore}", False, 'center', font=('Arial', 16, 'bold'))

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over!", False, 'center', font=('Arial', 16, 'bold'))

    def resetScore(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.clear()
        self.write(f"Score = {self.score} Highscore = {self.highscore}", False, 'center', font=('Arial', 16, 'bold'))

    def update_score(self):
        self.score+=1
        self.clear()
        self.write(f"Score = {self.score} Highscore = {self.highscore}", False, 'center', font=('Arial', 16, 'bold'))
