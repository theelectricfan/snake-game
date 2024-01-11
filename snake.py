import turtle


class Snake:
    def __init__(self):
        self.snakebody = []
        snake = turtle.Turtle(shape="triangle")
        snake.penup()
        snake.setposition(0, 0)
        snake.color("white")
        self.snakebody.append(snake)
        for n in range(1, 3):
            snake = turtle.Turtle(shape="square")
            snake.penup()
            snake.setposition(-20 * n, 0)
            snake.color("white")
            self.snakebody.append(snake)

    def extend(self):
        snake = turtle.Turtle(shape="square")
        snake.penup()
        snake.goto((self.snakebody[-1].position()))
        snake.color("white")
        self.snakebody.append(snake)

    def move(self):
        for n in range(len(self.snakebody) - 1, 0, -1):
            self.snakebody[n].goto(self.snakebody[n - 1].position())
        self.snakebody[0].forward(20)

    def goup(self):
        if self.snakebody[0].heading() == 270:
            return
        self.snakebody[0].setheading(90)

    def godown(self):
        if self.snakebody[0].heading() == 90:
            return
        self.snakebody[0].setheading(270)

    def goleft(self):
        if self.snakebody[0].heading() == 0:
            return
        self.snakebody[0].setheading(180)

    def goright(self):
        if self.snakebody[0].heading() == 180:
            return
        self.snakebody[0].setheading(0)
