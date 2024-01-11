import turtle
import random


class Food(turtle.Turtle):
    def __init__(self, snakebody):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh(snakebody)

    def refresh(self, snakebody):
        coordinate_x = random.randint(-280, 280)
        coordinate_y = random.randint(-280, 280)
        for segment in snakebody:
            while coordinate_x == segment.xcor() and coordinate_y == segment.ycor():
                self.refresh(snakebody)

        self.setposition(coordinate_x, coordinate_y)
