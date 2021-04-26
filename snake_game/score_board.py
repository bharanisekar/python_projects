from turtle import Turtle
score = 0
style = ('Courier',16, 'italic')

top = (0,275)
class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score =0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.goto(top)
        self.color("white")
        self.write(f'score = {self.score}',font=style, align='center')
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f'score = {self.score} high_score = {self.high_score}', font=style, align='center')

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f'score = {self.score} high_score = {self.high_score}', font=style, align='center')


    # def game_over(self):
    #     self.color("white")
    #     self.goto(0,0)
    #     self.write("Game over", font=style, align='center')
    #     self.hideturtle()






