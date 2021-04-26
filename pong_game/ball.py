from turtle import Turtle
import random
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.goto(0,0)
        self.x_move = 10
        self. y_move = 10
        self.move_speed = 0.1

    def ball_move_right(self):
        ball_x = self.xcor() + self.x_move
        ball_y = self.ycor() + self.y_move
        self.penup()
        self.goto(ball_x, ball_y)

    def ball_bounce_y(self):
        self.y_move *= -1
        self.move_speed *=0.9
    def ball_bounce_x(self):
        self.x_move *=-1
        self.move_speed *=0.9

    def reset_ball(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.ball_bounce_x()


