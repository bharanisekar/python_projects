from turtle import Screen
from snake import Snake
from food import Food
from score_board import Score

import time
screen = Screen()
screen.setup(width=600, height=600)
screen.title("snake_game")
screen.bgcolor("black")
screen.tracer(0)
snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


start=True
while start:
    screen.update()
    time.sleep(0.2)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extended()
        score.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset_snake()

    for segment in snake.forw[1:]:
        if snake.head.distance(segment) < 10:
            print(snake.head.distance(segment))
            score.reset()
            snake.reset_snake()








# turtle2 = Turtle(shape="square")
# turtle2.penup()
# turtle2.goto(x=-20,y=0)
# turtle2.color("white")
# turtle3 = Turtle(shape="square")
# turtle3.penup()
# turtle3.goto(x=-40,y=0)
# turtle3.color("white")






screen.exitonclick()