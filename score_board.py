from turtle import Turtle


class ScoreBoard(Turtle):
    #    ScoreBoard class inherits from Turtle class to manage and display scores in the game.
    def __init__(self):
        super().__init__()
        self.penup()
        self.setposition(-40, 280)
        self.hideturtle()
        self.color("white")
        self.score = 0
        self.high_score = 0
        self.show()

    def show(self):
        # Displays the current score and high score on the screen.
        try:
            with open("highscore.txt", mode="r") as high_sore:
                self.high_score = int(high_sore.read().strip() or 0)
        except (FileNotFoundError, ValueError):
            self.high_score = 0  # First run, or the file is empty or invalid
        self.write(f"             Score: {self.score}                 High Score: {self.high_score}", False,
                   align="center",
                   font=("Arial", 15, "normal"))

    def scoring(self):
        # Updates the score, checks for new high score, and updates display accordingly.
        self.score += 1
        if self.score > self.high_score:  # Update high score if current score is higher
            self.high_score = self.score
            with open("highscore.txt", mode="w") as high_sore:
                high_sore.write(f"{self.high_score}")  # Write new high score to file
        self.clear()  # Clear the previous score display
        self.show()  # Display updated score and high score on the screen
