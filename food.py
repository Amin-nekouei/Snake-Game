from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(.5, .5)
        self.penup()
        self.refresh()
        self.color("white")

    def refresh(self):
        self.setposition(x=random.randint(-250, 250), y=random.randint(-250, 250))
