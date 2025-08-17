# asteroids
Asteroids is a space-themed multidirectional shooter arcade video game. The player controls a single spaceship in an asteroid field which is periodically traversed by flying saucers. The object of the game is to shoot and destroy the asteroids.

## Demo
![Game play](gameplay.gif)

## Prerequisites
- Python 3.10+ installed
- ![uv](https://github.com/astral-sh/uv) project

## Before start

1. Create a virtual environment at the top level of your project directory:

```bash
uv venv
```

2. Activate the virtual environment:

```bash
source .venv/bin/activate
```

You should see (```Asteroids```) at the beginning of your terminal prompt

3. Install dependency:

```bash
uv sync
```

4. Run the game:

```bash
uv run main.py
```

## How to play
Using W, S to move up and down. A, D to turn direction and SPACE to shoot.
