from turtle import Turtle,Screen
segment = [(0, 0), (-20, 0), (-40, 0)]
moving_forward = 20
up=90
down = 270
left = 180
right = 0
class Snake:
    def __init__(self):
        self.forw = []
        self.shape_snake()
        self.head = self.forw[0]

    def shape_snake(self):
        for position in segment:
            self.add_forw(position)

    def add_forw(self,position):
        turtle1 = Turtle(shape="square")
        turtle1.penup()
        turtle1.goto(position)
        turtle1.color("white")
        self.forw.append(turtle1)

    def reset_snake(self):
        for self.forww in self.forw:
            self.forww.goto(1000,1000)
        self.forw.clear()
        self.shape_snake()
        self.head = self.forw[0]


    def extended(self):
        self.add_forw(self.forw[-1].position())

    def move(self):
        for seg in range(len(self.forw)- 1, 0, -1):
            x = self.forw[seg - 1].xcor()
            y = self.forw[seg - 1].ycor()
            self.forw[seg].goto(x, y)
        self.head.forward(moving_forward)

    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)

    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)

    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)

    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)