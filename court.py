from turtle import Turtle


class Court(Turtle):
    #Court class inherits from Turtle class to create a court area for the snake game.
    def __init__(self):
        super().__init__()
        self.penup()
        self.setposition(0, 270) #Sets initial position of the court (centered at the top)
        self.color("yellow")
        self.shape("square")
        self.upper_line()

    def upper_line(self):
        #Draws the upper boundary line of the court area.
        self.turtlesize(.25, 100) # Sets the size of the Turtle object (width, height)
