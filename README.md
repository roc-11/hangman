# Hangman Python Game

## Developer: Róisín O'Connell 

![Hangman Mockup Images]()

[View the live project here](https://hangman-roc-9218949e7f7b.herokuapp.com/)

[View GitHub repository](https://github.com/roc-11/hangman)

## Table of Contents

- [Hangman Python Game](#hangman-python-game)
  - [Developer: Róisín O'Connell](#developer-róisín-oconnell)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)

***

## Introduction
Hangman is a Python-based terminal game, which runs in the [Code Institute](https://codeinstitute.net/ie/ "Link to Code Institute homepage") mock terminal on [Heroku](https://www.heroku.com/ "Link to Heroku hompepage"). This project enables users to guess letters in order to reveal the mystery word. Users can select a level of difficulty and words are categorized into different categories. Users can make up to 6 incorrect guesses. Visual feedback is provided to users via ASCII Hangman illustrations for incorrect guesses.

The game was made for the third of five Milestone Projects required to complete the Diploma in Full Stack Software Development (e-Commerce Applications) program at [Code institute](https://codeinstitute.net/ie/ "Link to Code Institute homepage").

The main requirements of this project are to build a command-line application that is useful and usable, and allows users to manage a common dataset about a particular domain.

## How To Play
Hangman is a word guessing game where a player tries to reveal a hidden word by suggesting individual letters. And incorrect guess results in a piece of a hangman figure being drawn, while correct guesses reveal the guessed letter's position. You can read more about the Hangman game in general here (LINK).

Step by step version of how to play here

## Planning Stage

### Aim
The aim of this project is to build a Python-based Hangman game, which is fun and accessible to users, handles errors and is easy for users to navigate through the instructions. Users will play the game via a mock terminal on [Heroku](https://www.heroku.com/ "Link to Heroku hompepage").

### Application Goals
* To provide users with a terminal-based game of Hangman which they can play.
* To produce a Python-based Hangman game which both challenges and entertains users.
* To create an environment and rules that are easily interpreted and accessible for users.
* To implement error and exception handling to provide users with useful and informative feedback, and make for a better game experience.

### User Goals

## Features

### Main Menu

When a user launches the game, the main menu will be shown. A large ASCII Hangman Title is shown as well as some fun artwork. 
The user has 3 options to choose from on this first screen:
1. Play Game
2. Game Rules
3. Exit

User input is needed to proceed. The user can select 1, 2 or 3 and hit enter to proceed. 
The main_menu() function contains the code which deals with this initial screen. The list:

        valid_menu_selection = ['1', '2', '3']

is used to validate the user's selection. A selection entered outside of this list, e.g. 5 or "f", would result in an error message "INVALID CHOICE! Sorry, option not allowed." In this case, the user is again prompted to input a valid choice 1, 2, or 3. 

### Play Hangman

#### Category Selection 

#### Input Username

#### Generate Random, Mystery Word

#### Winner Screen

#### Game Over Screen

#### Play Again

### Game Rules 

### Exit Hangman

### Features to Implement in the Future

## Technologies Used

## Frameworks, Libraries & Programs Used

## Testing

## Bugs/Known Issues

## Deployment

## Credits

## Acknowledgements

