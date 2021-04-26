# import colorgram
# color_list=[]
# colors = colorgram.extract('61RQCX9SJKL.jpg', 25)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     col = (r, g, b)
#     color_list.append(col)
# print(color_list)
import turtle
from turtle import Turtle, Screen
import random
color_list = [(235, 234, 231), (234, 229, 231), (236, 35, 108), (221, 232, 237), (145, 28, 64), (239, 75, 35), (6, 148, 93), (232, 238, 234), (231, 168, 40), (184, 158, 46), (44, 191, 233), (27, 127, 195), (126, 193, 74), (253, 223, 0), (85, 28, 93), (173, 36, 97), (246, 219, 44), (44, 172, 112), (215, 130, 165), (215, 56, 27), (235, 164, 191), (156, 24, 23), (21, 188, 230), (238, 169, 157), (162, 210, 182)]
turtle.colormode(255)
tur = Turtle()
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     colours = (r,g,b)
#     return colours
def forw():
    tur.dot(10, random.choice(color_list))
    tur.penup()
    tur.hideturtle()
    tur.forward(50)

def mov():
    tur.left(90)
    tur.forward(50)
    tur.left(90)
    tur.forward(500)
    tur.right(90)
    tur.right(90)
s=True
x=0
tur.penup()
tur.hideturtle()
tur.setheading(225)
tur.forward(300)
tur.setheading(0)
while s:
    for i in range(10):
        tur.speed("fastest")
        forw()
    mov()
    x+=1
    if x==10:
        s=False






tur = Screen()
tur.exitonclick()