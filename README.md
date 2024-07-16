# Snake Game

This repository contains a simple implementation of the classic Snake game using Python's `turtle` graphics library. The game features a snake that moves around the screen, eats food to grow, and keeps track of the score.

## Project Structure

The project is organized into the following Python files:

1. **`snake.py`**: Defines the `Snake` class, which represents the snake and its movement.
2. **`food.py`**: Defines the `Food` class, which represents the food that the snake eats.
3. **`score_board.py`**: Defines the `ScoreBoard` class, which manages and displays the player's score.
4. **`court.py`**: Defines the `Court` class, which creates the game boundaries.
5. **`main.py`**: Initializes and runs the game, handling user input and game logic.

## Classes

### `Snake`

- **Purpose**: Represents the snake in the game.
- **Methods**:
  - `__init__()`: Initializes the snake and creates its body.
  - `build()`: Builds the initial segments of the snake.
  - `move()`: Moves the snake and handles screen boundaries.
  - `up()`, `down()`, `right()`, `left()`: Change the direction of the snake.
  - `get_big()`: Adds a segment to the snake's body.

### `Food`

- **Purpose**: Represents the food that the snake can eat to grow.
- **Methods**:
  - `__init__()`: Initializes the food with a circular shape and sets its initial position.
  - `refresh()`: Moves the food to a new random position.

### `ScoreBoard`

- **Purpose**: Displays and manages the score and high score.
- **Methods**:
  - `__init__()`: Initializes the scoreboard and loads the high score.
  - `show()`: Displays the current score and high score.
  - `scoring()`: Updates the score and checks if it surpasses the high score.

### `Court`

- **Purpose**: Creates the boundary of the game area.
- **Methods**:
  - `__init__()`: Initializes the court and draws the upper boundary line.


## Controls

- **Up Arrow**: Move the snake up.
- **Down Arrow**: Move the snake down.
- **Right Arrow**: Move the snake right.
- **Left Arrow**: Move the snake left.

## Notes

- The game will end if the snake collides with its own body.
- The score is saved in `highscore.txt`, which is updated whenever a new high score is achieved.
- The game window will close when you click on it.


