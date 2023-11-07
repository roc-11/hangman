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

## UX

### Planning Stage

#### Aim
The aim of this project is to build a Python-based Hangman game, which is fun and accessible to users, handles errors and is easy for users to navigate through the instructions. Users will play the game via a mock terminal on [Heroku](https://www.heroku.com/ "Link to Heroku hompepage").

#### Application Goals
* To provide users with a terminal-based game of Hangman which they can play.
* To produce a Python-based Hangman game which both challenges and entertains users.
* To create an environment and rules that are easily interpreted and accessible for users.
* To implement error and exception handling to provide users with useful and informative feedback, and make for a better game experience.

#### User Goals/Stories

New Users
- As a new site user, I would like to ____________, so that I can ____________.
- As a new site user, I would like to ____________, so that I can ____________.
- As a new site user, I would like to ____________, so that I can ____________.

Returning Users
- As a returning site user, I would like to ____________, so that I can ____________.
- As a returning site user, I would like to ____________, so that I can ____________.
- As a returning site user, I would like to ____________, so that I can ____________.

### User Feedback

### Flow Chart

## Features

### Main Menu

When a user launches the game, the main menu will be shown. A large ASCII Hangman Title is shown as well as some fun artwork. 
The user has 3 options to choose from on this first screen:
1. Play Game
2. Game Rules
3. Exit

User input is needed to proceed. The user can select 1, 2 or 3 and hit enter to proceed. 
The main_menu() function contains the code which deals with this initial screen. The list:

```
    valid_menu_selection = ['1', '2', '3']
```

is used to validate the user's selection. A selection entered outside of this list, e.g. 5 or "f", would result in an error message "INVALID CHOICE! Sorry, option not allowed." In this case, the user is again prompted to input a valid choice 1, 2, or 3. 

![screenshot - Main Menu](documentation/features-main-menu.png)

### Play Hangman

Selecting 1 from the main menu will begin the Hangman game. Three functions are run in this case:
1. get_rand_word()
2. welcome()
3. play_hangman(word)

The code will generate random word, show welcome, then play hangman. These will be further explained below. 

#### Category Selection & Generate Random, Mystery Word

The first part of playing the Hangman game involves a users being prompted to select a word category. There are 7 categories to choose from for this Hangman game. These are Countries, Sports, Zoo Animals, Fruit, Capital Cities (Europe), Harry Potter and Pokémon. 

In order to ensure a valid category is selected, there is a list: 

```
    valid_category = ["1", "2", "3", "4", "5", "6", "7"]
```

A while loop runs which prompts the user to select a category from the above list, input it and press enter. This input is stored as `category`. The while loop checks the value stored in `category`. If a valid number from the `valid_category` list is entered, the `words_list` variable is changed accordingly. There is a column for each category in `words_list` stored in the "words" sheet in Google Sheets Spreadsheets (LINK). Once a valid option is chosen, the loop is exited in order to proceed to generating a random word. 

The Python random (LINK) library is used to generate a random choice from the `words_list`. This random word is assigned to the variable `random_word`. The random word is then converted to a string with `str()` and made uppercase with `.upper()`. Finally, non-aphanumeric characters are removed from the random word string. (SEE BUGS FOR MORE DETAILS ON THIS)

```
return random word as string, remove non-alphanumeric characters

    word_to_string = str(random_word).upper()
    word_remove_non_alpha = filter(str.isalpha,word_to_string)
    word="".join(word_remove_non_alpha)

    return word
```

There is a defence included in case of an incorrect or invalid entry from the user. Anything entered which is not in the `valid_category` list will result in an error message in blue text appearing. The user will be again prompted to input a valid category selection. 

```
    elif category not in valid_category:
        print(f"{color_blue}Sorry, that is not a valid selection.")
        print(f"{color_blue}Only number 1 - 7 allowed.")
        time.sleep(2)  # delay message
        continue
```

![screenshot - Category Selection](documentation/features-category-selection.png)

#### Input Username

After a valid category is selected, the screen is cleared and there is a loading message, to delay all information appearing to the user at once. The time library (LINK) is imported at the top of the run.py file so that the `sleep()` function can be used throughout the game to delay/pause user feedback. 

The category the user selected is clarified. The user is then prompted to input their username. The reason for this is twofold:
* to provide a more personalised user experience (e.g. Congrats Colin!).
* initial plans included being able to save scores to Google Sheets. This turned out to be beyond the scope of this project.

The username prompt runs in a `while True:` loop. The `player_name` is returned and stored in the global variable `player_name` upon entering a valid username. 

Validation code is included here to prevent users entering 0 or an empty string. 
```
if len(player_name) == 0 or player_name == "":
    print(f"{color_blue}Sorry, you must enter a username!")
    continue
```
There is additional validation code to catch the error of a user entering a username which is non-alphabetic. 
```
elif not player_name.isalpha():
    print(f"{color_blue}Sorry, your name must be letters ONLY!")
    continue
```

The while loop runs until a valid username is entered and the user hits enter. 

![screenshot - Username](documentation/features-username.png)

#### Hangman Game Play Screen

The main Hangman game play screen begins with a friendly greeting message, personalised to the user (using the username entered on previous screen). This is followed by a "let's play Hangman" message. A message then appears informing the user that the secret word is loading from the `category` chosen for this round of game play. The user is also given information such as the number of letters in the mystery word.

![screenshot - Main Game Play 1 - Initial Game State](documentation/features-main-game-play-1.png)

Some variables are initialised at the beginning of play. Dashes are used to display the secret/mystery word to the user. The number of dashes is determined by the length of `word` (the variable generated by the `get_rand_word()` function. `word_length` stores the length of the mystery word so that a message is shown to make clear to the user how many letters are in the current mystery word. Upon load the user hasn't made any guesses yet, so `guessed` is set to 'False' and an empty array is declared to store the letters the user guesses during gameplay (`guessed_letters`). Finally, a user begins with 6 `tries` or lives. They have 6 lives to use, or incorrect guesses to make, before the Hangman is hanged. 

```
    word_completion = "_" * len(word)
    word_length = len(word)
    guessed = False
    guessed_letters = []
    tries = 6
```

The majority of the game play screen consists of the ASCII Hangman artwork. This shows a 'Nintendo'-style castle, tree and the empty hangman hanging platform. A function `display_hangman(tries)` contains an array `stages` which stores the artwork for each stage of the Hangman hanging. During gameplay, if the user makes an incorrect guess, the `tries` variable is decremented by 1 and the `display_hangman` fuction is called, with the `tries` variable as an argument. This ensures the correct array index artwork is shown, depending on how many incorrect guesses the user has made. Thus, each time the game screen is reprinted, the next ASCII artwork in the array is called (if the guess is incorrect). The artwork will remain if the guess is correct.

The game play runs in a loop `while not guessed and tries > 0:`. The code runs as follows: 

* User is prompted to guess a letter. This is validated to ensure only 1 letter is entered at a time and that the input is alphabetical (not a number, etc.).  `if len(guess) == 1 and guess.isalpha():`

* Invalid entries will result in an error message and user will be re-prompted to guess a letter 
    
    ```
    elif len(guess) > 1: 
        print(f"{color_blue}Sorry, only 1 letter at a time is allowed!")
    else:
        print(f"{color_blue}Not a valid guess. Only letters allowed!")
    ```

* There are some nested if/elif/else statements if a valid guess is made. 

    * if the user guesses a letter which they have already guessed, feedback will be given telling them this. 
       
        ```
        if guess in guessed_letters:
            print(f"{color_blue}You already guessed the letter {guess}")
        ```

    * if an INCORRECT guess has been made, i.e. the letter guess is NOT in the mystery word, a message will appear in RED informing the user of their incorrect guess. The number of `tries` is decrememted by one - user loses a life and a Hangman stage is drawn, and the incorrect guessed letter is pushed into the `guessed_letters` array.

        ```
        elif guess not in word:
            print(f"{color_red}{guess} is not in the word.")
            tries -= 1  # decrement the number of tries
            guessed_letters.append(guess)
        ```

    ![screenshot - Main Game Play 1 - Incorrect Guess](documentation/features-main-game-play-3.png)

    * if a CORRECT guess is made by the user, i.e. the letter guess is in the mystery word, a message will appear in GREEN informing the user of their correct guess. The correctly guessed letter is pushed into the `guessed_letters` array. The correctly guessed letter is then processed so that it is inserted into the word in the correct index place - so that the dash in the mystery word can be replaced by the CORRECT letter. So the `word_completion` variable is updated, replacing a dash with the correct letter.
        
        ```
        else:
            print(f"{color_green}Well done! {guess} is in the word!")
            guessed_letters.append(guess)
            word_as_list = list(word_completion)
            indices = [i for i, letter in enumerate(word) if letter == guess]
            for index in indices:
                word_as_list[index] = guess
            word_completion = "".join(word_as_list)
        ```

    ![screenshot - Main Game Play 2 - Correct Guess](documentation/features-main-game-play-2.png)

    * it is now possible that the user's CORRECT guess completes the word! If there are no more dashes remaining in `word_completion`, all the letters in the mystery word have been correctly guessed. `guessed` variable is changed to True and the user has saved the Hangman and won the game!
        
        ```
        if "_" not in word_completion:
            guessed = True
        ```

After each iteration of the main gameplay loop, or each user guess, feedback is provided to the user. The number of tries/lives remaining is shown in CYAN coloured text. The length of the mystery word is shown in MAGENTA. The Hangman is drawn, and `word_completion` is shown (with _ or correct letters or a combination, depending on state of game play).

#### Winner Screen

If the variable `guessed` equals True, the player/user wins. `guessed` only returns True when all the letters are guessed correctly in the secret word, so `word_completion` no longer contains dashes '_' (as explained ABOVE LINK).

If the user wins, the terminal is first cleared in order to provide the relevant congratulatory feedback. `WIN_ART` shows a large ASCII banner 'WINNER' text in green font. This is followed by `WINNER_ART` below the text, which displays a fun ASCII Hangman artwork, consisting of the menu art edited to show the Hangman saying "I'm free!" and "not hanged!". For additional user feedback and an extra-personal touch, a message displaying "congrats" and the `user_name` appears. Finally the mystery word the player guessed is also revealed here in the congratulatory message. 

``` 
    if guessed:
        clear_terminal()
        print(f"{color_green}{WIN_ART}")
        print(WINNER_ART)
        print(f"{color_green}Congrats {player_name}! You win! :) ")
        print(f"{color_green}Woohoo...you saved the Hangman by guessing the word {word}!")
        play_hangman_again()
```
![screenshot - Game Win](documentation/features-game-win.png)

#### Game Over Screen

If the variable `guessed` does not equal True and number of tries is zero (no lives remaining), the player/user loses and it is GAME OVER. The player has failed to guessed the mystery word, has incorrecly guessed 6 letters and the Hangman is hanged. 

If the user loses, the terminal is first cleared in order to provide the relevant sympathetic feedback. `LOSE_ART` shows a large ASCII banner 'GAME OVER' text in green font. This is followed by the code `display_hangman(tries)`, which calls the `display_hangman()` function, referencing the variable tries as a parameter. At this stage the value of `tries` is zero, as all lives have been used. So `stages[0]` is referenced from the stages array within the function. This shows the hanged Hangman in it's final state - head, torso, both arms, and both legs. For additional user feedback and an extra-personal touch, a message displaying "Sorry, the hangman has been hanged" and the `user_name` appears. Finally the mystery word is revealed to the user. 

``` 
    else:
        clear_terminal()
        print(f"{color_red}{LOSE_ART}")
        print(display_hangman(tries))
        print(f"{color_red}Oh no! The Hangman has been hanged! :( ")
        print(f"{color_red}Sorry {player_name}, you ran out of tries.")
        print(f"\nThe word was {word}. Maybe next time.")
        play_hangman_again()
``` 

![screenshot - Game Loss](documentation/features-game-over.png)

#### Play Again

Whether the user wins or loses, the same function is run after revealing the mystery word in order to give the user a choice on how to proceed:
`play_hangman_again()`

The purpose of this is to ask the user if they would like to play Hangman again, thus starting a new round of the game, or not. 

The user input prompt runs in a 'while True' loop. They can enter either Y for yes or N for n. 
```
    while True:
        play_again = input("Would you like to play Hangman again? Y or N: \n")
```

If the user enters 'Y' the terminal is cleared, a new mystery word in generated and `play_hangman(word)` is called, beginning a new Hangman game. This will repeat from LINK TO LINK ABOVE. 

```
    if play_again.upper() == "Y":
        clear_terminal()
        word = get_rand_word()
        play_hangman(word)
```

Or else if the user enters 'N', the user will be taken back to the main menu where they can exit the game (3) LINK, get instructions (2) LINK or chooise to play Hangman again (1) LINK TO LINK ABOVE. 

```
    elif play_again.upper() == "N":
        main_menu()
```

The `play_again` user input is cast to uppercase to deal with the case of the user inputting a lowercase 'y' or 'n' on the keyboard, which is quite likely. 

There is additional validation code included to account for an error, whereby the user enters something other than 'Y' or 'N', e.g. a number like 1, an empty string or the letter 'T'. In this instance a blue message will appear indicating that the response is invalid. The loop continues to prompt the user to input a valid response. 

```
    else:
        print(f"{color_blue}Sorry, only Y or N is a valid response.")
        continue  
```

![screenshot - Play Again](documentation/features-play-again.png)

### Game Rules 

It is vital that a user can view the game instructions so that they can gain optimal enjoyment and use of the Hangman game. 

Users can view the game instructions/rules from the main menu, by selecting option '2'. When a user inputs 2 the `menu_option` variables becomes 2, resulting in the `show_instructions()` function being called. 

```
    elif menu_option == '2':
        show_instructions()
```

Firstly, the `show_instructions()` function calls `clear_terminal()` so as to declutter the screen for ease of user viewing. Next the `RULES_ART` is printed, which is a large ASCII artwork title heading. Following this a multiple line string of text is displayed informing the user of how the game works, the game rules and how to win/lose the game (the Hangman game outcomes). You can read these rules from the screenshot below. 

![screenshot - Games Rules/Instructions](documentation/features-game-rules.png)

To return to the main menu the user is told to hit the return key. If the user enters anything other than return, an invalid choice error message is displayed and the user is prompted to enter the correct key. 

```
    while True:
        return_to_menu = input("Press Enter to return to the main menu. \n")
        if return_to_menu == "":
            main_menu()
            break
        else:
            print(color_blue + "INVALID CHOICE! Sorry, option not allowed.")
```

### Exit Hangman

When a user no longer wants to play Hangman they can choose to exit the game. This is an option on the main menu.

Users can exit the game from the main menu, by selecting option '3'. When a user inputs 3 the `menu_option` variables becomes 3, resulting in a number of outcomes. A user-friendly, informative message is first printed. Then the user is informed that the game is now exiting... `time.sleep(4)` pauses the execution of the code and results in a short pause while the user reads the aforementioned messages. Finally the screen is clearer and `exit()` is callled, to close the game/stop execution of `run.py`.

```
    elif menu_option == '3':
        print("______________________________\n")
        print("Thanks for visiting! See you next time.")
        print("Exiting game now...")
        time.sleep(4)  # delay exit for 3 seconds to show message
        clear_terminal()
        exit()
```
![screenshot - Exit](documentation/features-exit-hangman.png)

### Clear Terminal 

The code for clearing the terminal screen was sourced from [Geeks for Geeks](https://www.geeksforgeeks.org/clear-screen-python/). It is utilised throughout the `run.py` Python file in order to clear the screen/terminal for the user. It makes each step of gameplay clearer, allows for clearer user feedback and error messages, declutters the screen and improves the overall user experience. It is a vital function for the Hangman game to run smoothly and be an effective game. 

```
def clear_terminal():
    >>  for windows
    if name == 'nt':
        _ = system('cls')

    >>  for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
```

### Features to Implement in the Future

## Technologies Used

## Frameworks, Libraries & Programs Used

## Testing

## Bugs/Known Issues

## Deployment

Code Institute has provided a [template](https://github.com/Code-Institute-Org/python-essentials-template) to display the terminal view of this backend application in a modern web browser.
This is to improve the accessibility of the project to others.

The live deployed application can be found deployed on [Heroku](https://hangman-roc-9218949e7f7b.herokuapp.com).

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set the value of KEY to `PORT`, and the value to `8000` then select *add*.
- If using any confidential credentials, such as CREDS.JSON, then these should be pasted in the Config Variables as well.
- Further down, to support dependencies, select **Add Buildpack**.
- The order of the buildpacks is important, select `Python` first, then `Node.js` second. (if they are not in this order, you can drag them to rearrange them)

Heroku needs two additional files in order to deploy properly.

- requirements.txt
- Procfile

You can install this project's **requirements** (where applicable) using:

- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

- `pip3 freeze --local > requirements.txt`

The **Procfile** can be created with the following command:

- `echo web: node index.js > Procfile`

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:

- Select **Automatic Deployment** from the Heroku app.

Or:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (replace *app_name* with your app name)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The frontend terminal should now be connected and deployed to Heroku!

### Local Deployment

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the *requirements.txt* file.

- `pip3 install -r requirements.txt`.

If using any confidential credentials, such as `CREDS.json` or `env.py` data, these will need to be manually added to your own newly created project as well.

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/roc-11/hangman) 
2. Locate the Code button above the list of files and click it 
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
	- `git clone https://github.com/roc-11/hangman.git`
7. Press Enter to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/roc-11/hangman)

Please note that in order to directly open the project in Gitpod, you need to have the browser extension installed.
A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/roc-11/hangman)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

## Credits

## Acknowledgements

