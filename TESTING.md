# Testing

Return back to the [README.md](README.md) file.

## Code Validation

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |
| run.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/roc-11/hangman/main/run.py) | ![screenshot](documentation/py-validation-run.png) | Pass: No Errors |

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Hangman Game | Notes |
| --- | --- | --- | --- | --- | --- |
| ![Chrome](documentation/test-chrome.png) | Works as expected |
| ![Firefox](https://raw.githubusercontent.com/TravelTimN/markdown-builder/main/assets/img/firefox.png) | Works as expected |
| ![Edge](https://raw.githubusercontent.com/TravelTimN/markdown-builder/main/assets/img/edge.png) | Works as expected |
| ![Safari](documentation/test-safari.png) | Loads as expected, mock terminal does not work. Not compatible |

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Mobile | Desktop | Notes |
| --- | --- | --- | --- |
| run.py | ![screenshot](documentation/lighthouse-home-mobile.png) | ![screenshot](documentation/lighthouse-home-desktop.png) | Some minor warnings |

## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

| Page | Expectation | Test | Result | Fix | Screenshot | Screenshot |
| --- | --- | --- | --- | --- | --- | --- |
| Main Menu | | | | | | |
| | Feature is expected to start the Hangman game when the user does enters 1 | Tested the feature by doing entering 1 | The feature behaved as expected, and it did brought me to the category selection screen (game start) | Test concluded and passed | ![screenshot](documentation/features-main-menu.png) to | ![screenshot](documentation/features-category-selection.png) |
| | Feature is expected to do go to the rules/instructions screen when the user does enters 2 | Tested the feature by doing entering 2 | The feature behaved as expected, and it did brought me to the rules screen | Test concluded and passed | ![screenshot](documentation/features-main-menu.png) | ![screenshot](documentation/features-game-rules.png) |
| | Feature is expected to do go to display an error message when the user enters an invalid option, e.g. a number aside from 1,2,3 or a word/letter | Tested the feature by entering number 9 and word pizza. | The feature behaved as expected, and displayed the error message "INVALID CHOICE!" | Test concluded and passed | ![screenshot](documentation/main-menu-invalid-choice-1.png) | ![screenshot](documentation/main-menu-invalid-choice-2.png) |
| Rules/Instructions | | | | | | |
| | Feature is expected to return to the main menu when the user hits the enter key | Tested the feature by pressing the enter key | The feature behaved as expected and returned to the main menu. | Test concluded and passed | ![screenshot](documentation/features-game-rules.png) | ![screenshot](documentation/features-main-menu.png) |
| | Feature is expected to do display an error message when the user enters an invalid option (anything other than the enter key) | Tested the feature by doing entering the number 7 and the letter f. | The feature behaved as expected, and displayed the error message "INVALID CHOICE!" | Test concluded and passed | ![screenshot](documentation/testing-rules-error-1.png) | ![screenshot](documentation/testing-rules-error-2.png) |
| Category Selection | | | | | | |
| | Feature is expected to store the selected category and proceed to the username screen when the user  inputs number 1,2,3,4,5,6, or 7 | Tested the feature by entering each of the valid number options 1-7 | The feature behaved as expected and proceeded to the username screen. | Test concluded and passed | ![screenshot](documentation/testing-category.png) | ![screenshot](documentation/testing-username.png) |
| | Feature is expected to do display an error message when the user enters an invalid option (not number 1 - 7) | Tested the feature by doing entering the number 8 and the letter r. | The feature behaved as expected, and displayed the error message "Sorry, that is not a valid selection!" | Test concluded and passed | ![screenshot](documentation/testing-category-error-1.png) | ![screenshot](documentation/testing-category-error-2.png) |
| Username | | | | | | |
| | Feature is expected to store the username and proceed to the main Hangman game screen when the user inputs a vaild name (a letter or letters only) | Tested the feature by entering a valid name Roisin | The feature behaved as expected and proceeded to the Hangman game screen. | Test concluded and passed | ![screenshot](documentation/testing-username-2.png) | ![screenshot](documentation/testing-username-1.png) |
| | Feature is expected to do display an error message when the user enters an invalid option username (empty string, number) | Tested the feature by doing entering the number 5 and an empty string/space. | The feature behaved as expected, and displayed the error message "Sorry, your name must be letters only!" | Test concluded and passed | ![screenshot](documentation/testing-username-error-1.png) | ![screenshot](documentation/testing-username-error-2.png) |
| Main Game Play | | | | | | |
| | Feature is expected to say LETTER is NOT in the word and lose a try when the user inputs an incorrect guess. Also say LETTER is in the word and show the letter in it's correct space in the word if the guess was correct. | Tested the feature by entering a letter and getting expected response. | The feature behaved as expected. | Test concluded and passed | ![screenshot](documentation/testing-game-letter-1.png) | ![screenshot](documentation/testing-game-letter-2.png) |
| | Feature is expected to do display a message when the user enters a letter which they have already guessed. | Tested the feature by guessing the letter r and then guessing r again. | The feature behaved as expected, and displayed the message "You already guessed the letter R." | Test concluded and passed | ![screenshot](documentation/testing-game-same-letter-1.png) | ![screenshot](documentation/testing-game-same-letter-2.png) |
| | Feature is expected to do display an error message when the user enters more than one letter at a time or a full word. | Tested the feature by guessing the word IRELAND. | The feature behaved as expected, and displayed the message "Sorry, only 1 letter at a time is allowed." | Test concluded and passed | ![screenshot](documentation/testing-game-word-1.png) | ![screenshot](documentation/testing-game-word-2.png) |
| | Feature is expected to do display an error message when the user enters a number or an invalid key. | Tested the feature by guessing the number 3. | The feature behaved as expected, and displayed the message "Not a valid guess! Only letters allowed." | Test concluded and passed | ![screenshot](documentation/testing-game-num-1.png) | ![screenshot](documentation/testing-game-num-2.png) |
| Play Again | | | | | | |
| | Feature is expected to take the user to the main menu screen when the user enters N. | Tested the feature by entering N and was taken to the main menu. | The feature behaved as expected. | Test concluded and passed | ![screenshot](documentation/testing-play-again-n.png) | ![screenshot](documentation/features-main-menu.png) |
| | Feature is expected to take the user to play hangman again (categories screen) when the user enters Y. | Tested the feature by entering Y and was taken to the categories screen. | The feature behaved as expected. | Test concluded and passed | ![screenshot](documentation/testing-play-again-y.png) | ![screenshot](documentation/features-main-menu.png) |
| | Feature is expected to display an error message when the user enters an invalid input (only y or n allowed). | Tested the feature by entering the number 6 and the word 'no'. | The feature behaved as expected, and displayed the message "Sorry, only Y or N is a valid response." | Test concluded and passed | ![screenshot](documentation/testing-play-again-error-1.png) | ![screenshot](documentation/testing-play-again-error-2.png) |

## User Story Testing

| User Story | Screenshot |
| --- | --- |
| As a new site user, I would like to read the rules/instructions, so that I can learn how to play and understand the game correctly. | ![screenshot](documentation/features-game-rules.png) |
| As a new site user, I would like to have fun and be challenged, so that I can enjoy playing the game. | ![screenshot](documentation/features-main-game-play-1.png) |
| As a new site user, I would like a variety of word categories, so that I can replay the game many times. | ![screenshot](documentation/features-category-selection.png) |
| As a new site user, I would like to know how many guesses I have left when playing, so that I can be more tactical and careful with my guesses. | ![screenshot](documentation/features-game-feedback.png) |
| As a new site user, I would like feedback after my guess, so that I can adjust my game strategy. | ![screenshot](documentation/features-game-feedback.png) |
| As a new site user, I would like to be able to play again, so that I can improve my skills. | ![screenshot](documentation/features-play-again.png) |
| - As a returning site user, I would like to to have fun and be challenged, so that I can enjoy playing the game. | ![screenshot](documentation/features-main-game-play-1.png) |
| As a returning site user, I would like to a variety of word categories, so that I can replay the games and experience new words each time I play. | ![screenshot](documentation/features-category-selection.png) |
| As a returning site user, I would like feedback after my guess, so that I can adjust my game strategy. | ![screenshot](documentation/features-game-feedback.png) |
| As a returning site user, I would like to be able to play again, so that I can improve my skills. | ![screenshot](documentation/features-play-again.png) |
| As a site administrator, I should be able to add words to the Google Sheet, so that I can extend the game and implement difficulty levels in the future. | ![screenshot](documentation/google-sheet-scalable.png) |

## Bugs

- Python `'ModuleNotFoundError'` when trying to import module from imported package

    ![screenshot](documentation/bug03.png)

    - To fix this, I _____________________.

- Python `E501 line too long` (93 > 79 characters)

    ![screenshot](documentation/bug04.png)

    - To fix this, I _____________________.

- Python `E501 line too long` (whitespace error)

    ![screenshot](documentation/bug04.png)

    - To fix this, I _____________________.

## Unfixed Bugs

- For PP3, when using a helper `clear()` function, any text above the height of the terminal does not clear, and remains when you scroll up.

    ![screenshot](documentation/unfixed-bug02.png)

    - Attempted fix: I tried to adjust the terminal size, but it only resizes the actual terminal, not the allowable area for text.

There are no remaining bugs that I am aware of.
