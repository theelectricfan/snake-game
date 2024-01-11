import turtle


class Wall(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-300, 300)
        self.pendown()
        self.width(20)
        self.color('orange')
        for n in range(4):
            self.forward(2 * 300)
            self.right(90)
