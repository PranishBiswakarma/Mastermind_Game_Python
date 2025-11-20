# Mastermind Game in Python

A command-line implementation of the classic code-breaking game Mastermind. The game challenges the player to guess a randomly generated color pattern within a limited number of attempts.

## Features

- Generates a random code of colored pegs for the player to guess.
- Provides feedback on the number of correctly positioned colors and correct colors in the wrong position after each guess.
- Tracks attempts and informs the player of remaining tries.
- Simple, beginner-friendly Python implementation suitable for learning game logic and core programming concepts.

## How to Play

1. The game will generate a secret code of 4 colors chosen from:
   - R (Red)
   - G (Green)
   - B (Blue)
   - Y (Yellow)
   - W (White)
   - O (Orange)
2. Enter your guess as four color codes separated by spaces, e.g., `R G B Y`.
3. After each guess, you'll see feedback:
   - The number of colors guessed correctly in the correct position.
   - The number of correct colors guessed but in the wrong position.
4. You have 10 attempts to guess the correct code.

## Setup & Usage

1. Save the script as `mastermind.py`.
2. Run the script from your terminal:
python mastermind.py
3. Follow on-screen prompts to input guesses.

## Skills Demonstrated

- Python basics and control structures.
- Random module usage for code generation.
- Input validation and user interaction.
- Implementing game logic with loops and conditionals.
- Code organization using functions.

## Notes

- The game is fully standalone and requires no external libraries.
- Try modifying the `COLORS`, `TRIES`, or `CODE_LENGTH` variables to customize difficulty.
