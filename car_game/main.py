from turtle import Turtle, Screen
from tur import Tur
from car import Car
import time
import random

screen = Screen()
screen.title("Car Hit Game")
screen.setup(height=350,width=400)
screen.tracer(0)

tur = Tur()
car = []
colors=['red','orange','yellow','green','blue','purple']
for i in range(6):
    cars = Turtle(shape="square")
    cars.shapesize(stretch_wid=0.7, stretch_len=1.7)
    cars.color(colors[i])
    cars.penup()
    cars.goto(x=200,y=random.randint(-120,120))
    car.append(cars)


screen.listen()
screen.onkey(tur.up,"Up")

game = True
while game:
    screen.update()
    time.sleep(1)
    for j in car:
        j.backward(random.randint(0,50))
    if tur.ycor() > 150:
        game = False
        print("hit the wall")

    if tur.distance(j) < 10:
        print(tur.distance(j))
        game = False
        print("hit the wall")











screen.exitonclick()