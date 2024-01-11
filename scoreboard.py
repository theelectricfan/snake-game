import turtle


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.hideturtle()
        self.penup()
        self.goto(0,250)
        self.color("aqua")
        self.write(f"Score = {self.score}", False, 'center', font=('Arial', 16, 'bold'))

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over!", False, 'center', font=('Arial', 16, 'bold'))

    def update_score(self):
        self.score+=1
        self.clear()
        self.write(f"Score = {self.score}", False, 'center', font=('Arial', 16, 'bold'))
