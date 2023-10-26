# Hangman

# Hangman Game

This is a simple command-line Hangman game implemented in Python. You can play it either in single-player mode or two-player mode.

## Table of Contents
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Game Rules](#game-rules)
- [Single-Player Mode](#single-player-mode)
- [Two-Player Mode](#two-player-mode)
- [Commands](#commands)
- [Ending the Game](#ending-the-game)

## Installation <a name="installation"></a>

To play this Hangman game, you need to have Python installed on your computer. Follow these steps to get started:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/your-username/hangman-game.git


# How to Play <a name="how-to-play"></a>
Hangman is a word-guessing game where one player thinks of a word and the other player tries to guess it by suggesting letters one at a time. The game ends when the guesser correctly guesses the word or runs out of allowed incorrect guesses.

# Game Rules <a name="game-rules"></a>
1. The word to be guessed is represented by a series of dashes, each dash representing a letter.

2. The guesser (or guessers) can input a letter to guess. The game checks if the letter is in the word.

3. If the guessed letter is correct, the letter is revealed in the word.

4. If the guessed letter is incorrect, the game keeps track of the number of incorrect guesses. The Hangman image is displayed with each incorrect guess.

5. The game continues until either the word is completely guessed, or the number of incorrect guesses reaches a certain limit.

# Single-Player Mode <a name="single-player-mode"></a>
**In single-player mode, the game selects a random word from a predefined list of words. The player has to guess the letters to complete the word.**

# Two-Player Mode <a name="two-player-mode"></a>
**In two-player mode, one player thinks of a word and enters it. The other player tries to guess the word by suggesting letters one at a time.**

# Commands <a name="commands"></a>
1. The game accepts the following commands:

2. Guess a letter: Input a single letter to guess. The game will inform you if the letter is in the word.

3. let me see: Reveals the word when entered. Useful if you're stuck.

4. reset: Resets the number of incorrect guesses to zero.

5. set: Allows you to set the number of tries (incorrect guesses) for the game.

# Ending the Game <a name="ending-the-game"></a>
The game ends when one of the following conditions is met:

The game ends when you correctly guess the word or exceed the allowed number of incorrect guesses.

You can also manually end the game by entering xna at any time.
