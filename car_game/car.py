from turtle import Turtle

class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.colors = ['red','orange','yellow','green','blue','purple']
        self.ranges = [-70, -100, -130, -50, -30,-45]
        cars=[]
        for i in range(6):
            self.shape("square")
            self.shapesize(stretch_wid=0.7, stretch_len=2)
            self.color(self.colors[i])
            self.penup()
            self.goto(x=0, y=self.ranges[i])
            cars.append()

    # def car_shape(self):
    #     self.shape("square")
    #     self.shapesize(stretch_wid=0.7, stretch_len=2)
    #     self.color("red")
    #     self.penup()
    #     self.goto(20,0)
