from turtle import Turtle


class T_turtle(Turtle):
    def __init__(self):
        super().__init__()
        self.create_body()

    def create_body(self):
        self.shape("turtle")
        self.penup()
        self.goto(0, -280)
        self.setheading(90)

