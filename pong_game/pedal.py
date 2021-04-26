from turtle import Turtle

class Pedal(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)

    def up(self):
        new_position = self.ycor() + 20
        self.goto(self.xcor(), new_position)

    def down(self):
        new_position = self.ycor() - 20
        self.goto(self.xcor(), new_position)



