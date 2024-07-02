from turtle import Turtle


class Snake:
    # Snake class inherits from Turtle class to represent a snake object in the game.
    def __init__(self):
        self.body = []
        self.build()
        self.head = self.body[0]

    def build(self):
        #Creates initial segments of the snake's body.
        initial_x = 0
        for kafi in range(0, 3):
            kafi = Turtle("square")
            kafi.color("white")
            kafi.penup()
            kafi.setposition(initial_x, 0)
            initial_x -= 20
            self.body.append(kafi)

    def move(self):
        # Move each segment of the snake's body to the position of the segment in front of it
        for index in range(len(self.body) - 1, 0, -1):
            # self.body[index].showturtle()
            new_x = self.body[index - 1].xcor()
            new_y = self.body[index - 1].ycor()
            self.body[index].setposition(new_x, new_y)
        # Move the snake's head forward in its current direction
        self.head.forward(20)
        # Boundary checking (wrap around screen edges)
        if self.head.xcor() > 290:
            self.head.setx(-290)
        if self.head.xcor() < -290:
            self.head.setx(290)
        if self.head.ycor() > 250:
            self.head.sety(-310)
        if self.head.ycor() < -310:
            self.head.sety(250)

    def up(self):
        # Change snake's direction to up
        if self.head.heading() != 270:
            self.head.seth(90)

    def down(self):
        # Change snake's direction to down
        if self.head.heading() != 90:
            self.head.seth(270)

    def right(self):
        # Change snake's direction to right
        if self.head.heading() != 180:
            self.head.seth(0)

    def left(self):
        if self.head.heading() != 0:
            # Change snake's direction to left
            self.head.seth(180)

    def get_big(self):
        # Add a new segment to the snake's body when it eats food
        kafi = Turtle("square")
        kafi.penup()
        kafi.color("white")
        kafi.goto(self.body[-1].position())
        self.body.append(kafi)
