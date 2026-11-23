# Snake Game

The classic Snake arcade game, written in Python with the `turtle` graphics module and an object-oriented design.

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white) ![turtle](https://img.shields.io/badge/Graphics-turtle-informational)

## Features

- Arrow-key controls, with the snake wrapping around the edges of the board.
- The snake grows and the score goes up each time it eats food, which then reappears at a random position.
- The game ends when the snake runs into its own body.
- The high score is saved to `highscore.txt` and kept between sessions; the file is created on the first run.

## Design

Each part of the game is its own class, and `main.py` only runs the game loop:

| File | Class | Responsibility |
|---|---|---|
| `snake.py` | `Snake` | Body segments, movement, direction changes, growing |
| `food.py` | `Food` | Food placement |
| `score_board.py` | `ScoreBoard` | Current score, persistent high score |
| `court.py` | `Court` | Draws the play area |
| `main.py` | – | Screen setup, key bindings, game loop and collision checks |

## Run it

Only the Python standard library is needed (Python 3.8+).

```bash
git clone https://github.com/Amin-nekouei/Snake-Game.git
cd Snake-Game
python main.py
```

Use the arrow keys to steer. Click the window to close it after the game ends.

## Author

**Amin Nekouei** · [LinkedIn](https://www.linkedin.com/in/amin-nekouei) · [GitHub](https://github.com/Amin-nekouei)
