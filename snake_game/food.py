from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.shapesize(0.3,0.3)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-285, 270)
        random_y = random.randint(-285, 270)
        self.goto(random_x,random_x)



