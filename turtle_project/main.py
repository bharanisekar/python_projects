from turtle import Turtle, Screen
import turtle
import random
tur = Turtle()
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colours = (r,g,b)
    return colours

def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        tur.speed("fastest")
        tur.color(random_color())
        tur.circle(100)
        tur.setheading(tur.heading() + size_of_gap)
draw_spirograph(5)

#
#
# tur.shape("arrow")
# tur.pensize(8)
# tur.speed("fastest")
#
# # random walk
# degree = [0, 90,180,270]
# for i in range(200):
#     tur.color(random_color())
#     tur.forward(10)
#     tur.setheading(random.choice(degree))#direction turtle is facing all angles like right,left
#
#

#angles triangle to pentogan
# colours = ["#FFA07A","#FFD700","#556B2F","#556B2F"]
# def angles(need_angle):
#     angle = 360 / need_angle
#     for i in range(need_angle):
#         tur.pensize(10)
#         tur.forward(100)
#         tur.right(angle)
#
# for i in range(3,11):
#     tur.color(random.choice(colours))
#     angles(i)


# dahsed lines
# for i in range(4):
#     tur.forward(10)
#     tur.penup()   #--->penup means no line it produces
#     tur.forward(10)
#     tur.pendown() #-->pendown means it produces line


# square shape
# for i in range(4):
#     tur.forward(100)
#     tur.right(90)

tur = Screen()
tur.exitonclick()

