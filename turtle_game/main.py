from turtle import Turtle,Screen
import random

t = Screen()
t.setup(width=500, height=400)

user_answer=t.textinput(title="Game_starts", prompt="which color turtle is going to win")
turtless=[]
colors=['red','orange','yellow','green','blue','purple']
ranges=[-70, -100, -130, -50, -30, 0]
for i in range(6):
    tur = Turtle(shape="turtle")
    tur.color(colors[i])
    tur.penup()
    tur.goto(x=-240, y=ranges[i])
    turtless.append(tur)
is_race = True
while is_race:
    for j in turtless:
        j.forward(random.randint(1,10))
        j.speed("slow")
        if j.xcor() > 230:
            is_race = False
            win_color = j.pencolor()
            if win_color == user_answer :
                print(f"you win {win_color} turtle is winner")
            else:
                print(f"you loss {win_color} turtle is winner")





t.exitonclick()