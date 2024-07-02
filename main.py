from turtle import Screen
import time
from snake import Snake
from food import Food
from score_board import ScoreBoard
from court import Court

# Initialize the screen
screen = Screen()
screen.setup(width=600, height=640)
screen.bgcolor("black")
screen.tracer(0)

# Create instances of Snake, Food, ScoreBoard, and Court
snake = Snake()
food = Food()
score = ScoreBoard()
court = Court()

# Listen to key events
screen.listen()
# Define key bindings for controlling the snake's movement
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

# Initialize game loop
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.09) # Introduces a delay to control game speed
    snake.move()
# Check if snake collides with food
    if snake.head.distance(food) < 15:
        score.scoring()
        food.refresh()
        snake.get_big()
# Check if snake collides with its own body
    for part in snake.body[1:]:
        if part.distance(snake.head) < 10:
            game_is_on = False # End game if collision detected

# End the game when the loop ends
screen.exitonclick()
