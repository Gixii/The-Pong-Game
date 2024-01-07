from turtle import Turtle
Y_COR = 30


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.shape("square")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.color("white")
        self.goto(self.x, self.y)
        self.speed("fastest")

    def move_up(self):
        new_y = self.ycor() + Y_COR
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - Y_COR
        self.goto(self.xcor(), new_y)


