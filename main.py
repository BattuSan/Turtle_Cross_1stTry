from turtle import Turtle, Screen
from turtoise import T_turtle

screen = Screen()
screen.title("Turtle Cross")
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)

t_turtle = T_turtle()
game_is_on = True

while game_is_on:
    screen.update()
screen.exitonclick()
