from turtle import Turtle,Screen

import scoreboard
from pedal import Pedal
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(height=600, width=800)
screen.title("Pong Game")
screen.bgcolor("black")
screen.tracer(0)

r_pedal = Pedal((350, 0))
l_pedal = Pedal((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_pedal.up,"Up")
screen.onkey(r_pedal.down,"Down")
screen.onkey(l_pedal.up,"w")
screen.onkey(l_pedal.down, "s")

start=True
while start:
    screen.update()
    ball.ball_move_right()
    time.sleep(0.1)
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.ball_bounce_y()

    if ball.distance(r_pedal) < 50 and ball.xcor() > 320 or ball.distance(l_pedal)< 50 and ball.xcor() < -320:
        ball.ball_bounce_x()


    if ball.xcor() > 380:
        ball.reset_ball()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_ball()
        scoreboard.r_point()





screen.exitonclick()




