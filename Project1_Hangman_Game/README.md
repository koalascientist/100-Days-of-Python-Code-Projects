# Hangman Game

## Description of the game

Hangman is a game where a player needs to guess a word by suggesting letters given a certain number of attempts.

## Game rules

The game chooses a random word from **hangman_words** file. The word to guess is represented by a row of _ (i.e. underscores), representing each letter in the word. You have 6 lives in total to guess the correct word.

You will be asked to guess a letter. If you guess a letter which occurs in the word, then the letter will be written in all its correct positions in the word. In cases when you guess a letter that has been guessed before and occurs in the word, no life will be deducted. If you guess a wrong letter, then you will lose a life.

You win once you guess the word, and you lose once you have no more lives left.

## Code structure

**hangman_art.py** file contains the ASCII logo of the game and the ASCII representation of each stage of the game dependent on the number of lives left in the game.

**hangman_words.py** file contains the list of words that can be guessed while playing the game.

**hangman_code.py** file contains the Python code for the game.

! Please make sure to keep all files in one folder when running the game.
