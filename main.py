import turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from wall import Wall

turtle.mode("standard")
window = turtle.Screen()
window.setup(width=600, height=600)
window.bgcolor("black")
window.title("Snake game")
window.tracer(n=0)
window.listen()
snake = Snake()
food = Food(snake.snakebody)
wall = Wall()
scoreboard = Scoreboard()
window.onkey(fun=snake.goup, key="Up")
window.onkey(fun=snake.godown, key="Down")
window.onkey(fun=snake.goleft, key="Left")
window.onkey(fun=snake.goright, key="Right")
window.onkey(fun=snake.goup, key="w")
window.onkey(fun=snake.godown, key="s")
window.onkey(fun=snake.goleft, key="a")
window.onkey(fun=snake.goright, key="d")

window.update()


def game():
    snake.move()
    if snake.snakebody[0].distance(food) < 15:
        food.refresh(snake.snakebody)
        scoreboard.update_score()
        snake.extend()

    for segment in snake.snakebody[1:]:
        if snake.snakebody[0].distance(segment) < 10:
            scoreboard.game_over()
            return

    if snake.snakebody[0].xcor() > 280 or snake.snakebody[0].xcor() < -280 or snake.snakebody[0].ycor() > 280 or \
            snake.snakebody[0].ycor() < -280:
        scoreboard.game_over()
        return

    window.update()
    window.ontimer(game, 100)


game()

window.exitonclick()
