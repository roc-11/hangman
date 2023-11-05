'''
Hangman - A Python terminal game by Roisin O'Connell.
'''

import gspread
from google.oauth2.service_account import Credentials
import random
import re
from colorama import Fore, Back, Style, init
from os import system, name # import only system from os
import time 

#Initialize colorama, autoreset after each use of Colorama
init(autoreset=True)

#Google Sheet set up
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSREAD_CLIENT.open('hangman')

GAME_LOGO = """
    ██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗
    ██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║
    ███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║
    ██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║
    ██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║
    ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝
    """

RULES_ART = """
      _______  _______  _______  _______          _______           _        _______  _______ 
    (  ____ \(  ___  )(       )(  ____ \        (  ____ )|\     /|( \      (  ____ \(  ____ /
    | (    \/| (   ) || () () || (    \/        | (    )|| )   ( || (      | (    \/| (    \/
    | |      | (___) || || || || (__            | (____)|| |   | || |      | (__    | (_____ 
    | | ____ |  ___  || |(_)| ||  __)           |     __)| |   | || |      |  __)   (_____  )
    | | \_  )| (   ) || |   | || (              | (\ (   | |   | || |      | (            ) |
    | (___) || )   ( || )   ( || (____/\        | ) \ \__| (___) || (____/\| (____/\/\____) |
    (_______)|/     \||/     \|(_______/        |/   \__/(_______)(_______/(_______/\_______)
    """

WIN_ART = """
              _______                             _________ _        _  _ 
    |\     /|(  ___  )|\     /|          |\     /|\__   __/( (    /|( )( )
    ( \   / )| (   ) || )   ( |          | )   ( |   ) (   |  \  ( || || |
     \ (_) / | |   | || |   | |          | | _ | |   | |   |   \ | || || |
      \   /  | |   | || |   | |          | |( )| |   | |   | (\ \) || || |
       ) (   | |   | || |   | |          | || || |   | |   | | \   |(_)(_)
       | |   | (___) || (___) |          | () () |___) (___| )  \  | _  _ 
       \_/   (_______)(_______)          (_______)\_______/|/    )_)(_)(_)
    """

LOSE_ART = """
              _______                     _        _______  _______  _______  _  _ 
    |\     /|(  ___  )|\     /|          ( \      (  ___  )(  ____ \(  ____ \( )( )
    ( \   / )| (   ) || )   ( |          | (      | (   ) || (    \/| (    \/| || |
     \ (_) / | |   | || |   | |          | |      | |   | || (_____ | (__    | || |
      \   /  | |   | || |   | |          | |      | |   | |(_____  )|  __)   | || |
       ) (   | |   | || |   | |          | |      | |   | |      ) || (      (_)(_)
       | |   | (___) || (___) |          | (____/\| (___) |/\____) || (____/\ _  _ 
       \_/   (_______)(_______)          (_______/(_______)\_______)(_______/(_)(_)
    """                                                                           

MENU_ART = '''

                           __________   ▄▄▄▄▄▄
                          | HELP ME! |  |    █
                           ¯¯¯¯¯¯¯¯¯¯\\  °    █            ▒▒▒▒▒▒▒▒
               █▄██▄█                  \\O/   █           ▒▒▌▒▒▐▒▒▌▒
      █▄█▄█▄█▄█▐█┼██▌█▄█▄█▄█▄█          |    █            ▒▀▄▒▌▄▀▒
      ███┼█████▐████▌█████┼███         / \\   █               ██
░░░░░░█████████▐████▌█████████░░░░░░████████████░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
'''

def display_hangman(tries):
    stages = [# 6 final state: head, torso, both arms, and both legs
        '''
                        _______________   ▄▄▄▄▄▄
                        | OUCH MY NECK! |  |    █
                        ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯ \\  O    █            ▒▒▒▒▒▒▒▒
                █▄██▄█                    /|\\   █           ▒▒▌▒▒▐▒▒▌▒
        █▄█▄█▄█▄█▐█┼██▌█▄█▄█▄█▄█          / \\   █            ▒▀▄▒▌▄▀▒
        ███┼█████▐████▌█████┼███               █                 ██
    ░░░░░░█████████▐████▌█████████░░░░░░████████████░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
        ''',
        # 5 head, torso, both arms, and one leg
        '''
                                            ▄▄▄▄▄▄
                                            |    █
                                            O    █            ▒▒▒▒▒▒▒▒
                █▄██▄█                     /|\\   █           ▒▒▌▒▒▐▒▒▌▒
        █▄█▄█▄█▄█▐█┼██▌█▄█▄█▄█▄█           /     █            ▒▀▄▒▌▄▀▒
        ███┼█████▐████▌█████┼███               █                 ██
    ░░░░░░█████████▐████▌█████████░░░░░░████████████░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
        ''',
        # 4 head, torso, and both arms
        '''
                                            ▄▄▄▄▄▄
                                            |    █
                                            O    █            ▒▒▒▒▒▒▒▒
                █▄██▄█                     /|\\   █           ▒▒▌▒▒▐▒▒▌▒
        █▄█▄█▄█▄█▐█┼██▌█▄█▄█▄█▄█               █             ▒▀▄▒▌▄▀▒
        ███┼█████▐████▌█████┼███               █                 ██
    ░░░░░░█████████▐████▌█████████░░░░░░████████████░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
        ''',
        # 3 head, torso, and one arm
        '''
                                            ▄▄▄▄▄▄
                                            |    █
                                            O    █            ▒▒▒▒▒▒▒▒
                █▄██▄█                     /|    █           ▒▒▌▒▒▐▒▒▌▒
        █▄█▄█▄█▄█▐█┼██▌█▄█▄█▄█▄█               █            ▒▀▄▒▌▄▀▒
        ███┼█████▐████▌█████┼███               █                 ██
    ░░░░░░█████████▐████▌█████████░░░░░░████████████░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
        ''',
        # 2 head and torso
        '''
                                            ▄▄▄▄▄▄
                                            |    █
                                            O    █            ▒▒▒▒▒▒▒▒
                █▄██▄█                     |    █           ▒▒▌▒▒▐▒▒▌▒
        █▄█▄█▄█▄█▐█┼██▌█▄█▄█▄█▄█               █            ▒▀▄▒▌▄▀▒
        ███┼█████▐████▌█████┼███               █                 ██
    ░░░░░░█████████▐████▌█████████░░░░░░████████████░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
        ''',
        # 1 head
        '''
                                            ▄▄▄▄▄▄
                                            |    █
                                            O    █            ▒▒▒▒▒▒▒▒
                █▄██▄█                          █           ▒▒▌▒▒▐▒▒▌▒
        █▄█▄█▄█▄█▐█┼██▌█▄█▄█▄█▄█               █            ▒▀▄▒▌▄▀▒
        ███┼█████▐████▌█████┼███               █                 ██
    ░░░░░░█████████▐████▌█████████░░░░░░████████████░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
        ''',
        # 0 initial empty state
        '''
                                            ▄▄▄▄▄▄
                                            |    █
                                                █            ▒▒▒▒▒▒▒▒
                █▄██▄█                         █           ▒▒▌▒▒▐▒▒▌▒
        █▄█▄█▄█▄█▐█┼██▌█▄█▄█▄█▄█               █            ▒▀▄▒▌▄▀▒
        ███┼█████▐████▌█████┼███               █               ██
    ░░░░░░█████████▐████▌█████████░░░░░░████████████░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
        '''
    ]
    return stages[tries]

def clear_terminal():
    """
    Clears the terminal. Code from:
    https://www.geeksforgeeks.org/clear-screen-python/
    """
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def main_menu():
    """
    Main menu shown to user on startup.
    Provide user with 4 options
    """

    clear_terminal()

    print(GAME_LOGO)
    print(MENU_ART)
    print("Type 1: To play the game")
    print("Type 2: For game rules")
    print("Type 3: To exit")
    
    menu_options = input("Please choose an option 1, 2 or 3 and press Enter:\n")
    valid_menu_selection = ['1', '2', '3']

    if menu_options not in valid_menu_selection: #check user input is valid
        print(Back.BLUE + "INVALID CHOICE! Sorry, option not allowed.")
        print(Back.BLUE + "Please choose option 1, 2 or 3.")
        main_menu()
    elif menu_options == '1':
        word = get_rand_word()
        play_hangman(word)
    elif menu_options == '2':
        show_instructions()
    elif menu_options == '3':
        #clear the terminal and exit the game
        print("exit game now")
        clear_terminal()

def show_instructions():
    """
    Show user game instructions.
    User will access these by selecting "2" on main menu.
    """

    clear_terminal()

    print(RULES_ART)
    print(
        """
        This is a classic game of Hangman.
        Begin by pressing 1 on the main menu screen.
        First, choose a word category. The computer will then generate a 
        random mystery word from this category, with each letter shown as 
        an underscore (e.g. _ _ _ _ ). 
        The player must try to guess the word by typing one letter at a time.
        If the guess is correct, the letter will appear in the word.
        Each incorrect guess will cost you one of your 6 lives, and the 
        Hangman will start to be hanged!
        Once you run out of lives, the Hangman will die and you will lose
        the game :(
        To win: guess the word before your lives reach ZERO. :)
        The fate of the Hangman lies in your hands!! GOOD LUCK!! 
        """
    )

    while True:
        return_to_menu = input("Please press Enter to return to the main menu. \n")
        if return_to_menu == "":
            main_menu()
            break
        else:
            print(Back.BLUE + "INVALID CHOICE! Sorry, option not allowed.")


def welcome():
    """
    Welcome user to the game on start up.
    """
    print("______________________________\n")

    while True:
        name = input("Please enter your preferred game name:\n")
        #validate username
        if len(name) == 0 or name == "":
            print(f"{Back.RED+Style.BRIGHT}Sorry, you must enter a username!")
            continue
        elif not name.isalpha():
            print(f"{Back.RED+Style.BRIGHT}Sorry, your name must be letters ONLY!")
            continue
        else:
            print("______________________________\n")
            print("Greetings " + name + "! Glad to have you playing today!\n")
            return name

def get_rand_word():
    """
    Get user category selection.
    Get random word from Google Sheets words list.
    """
    global category_name
    clear_terminal()
    print(GAME_LOGO)
    print("WELCOME TO HANGMAN!")
    print("______________________________\n")
    
    print("CATEGORIES:")
    print("1. Countries")
    print("2. Sports")
    print("3. Zoo Animals")
    print("4. Fruit")
    print("5. Capital Cities (Europe)")
    print("6. Harry Potter")
    print("7. Pokémon")
    category = input("Please select a category from the choices above: \n")

    valid_category = ["1", "2", "3", "4", "5", "6", "7"]
    words_sheet = SHEET.worksheet('words')
    #check category selection is valid
    if category not in valid_category:
        print(f"{Back.YELLOW+Style.BRIGHT}Sorry, that is not a valid selection.")
        get_rand_word()
    elif category == "1":
        words_list = words_sheet.col_values(1)
        category_name = "Countries"
    elif category == "2":
        words_list = words_sheet.col_values(2)
        category_name = "Sports"
    elif category == "3":
        words_list = words_sheet.col_values(3)
        category_name = "Zoo Animals"
    elif category == "4":
        words_list = words_sheet.col_values(4)
        category_name = "Fruit"
    elif category == "5":
        words_list = words_sheet.col_values(5)
        category_name = "Capital Cities (Europe)"
    elif category == "6":
        words_list = words_sheet.col_values(6)
        category_name = "Harry Potter"
    elif category == "7":
        words_list = words_sheet.col_values(7)
        category_name = "Pokémon"
    #words_list = words_sheet.get_all_values()
    random_word = random.choice(words_list)

    #return random word as string, remove non-alphanumeric characters
    word_to_string = str(random_word).upper()
    word_remove_non_alpha = filter(str.isalpha,word_to_string)
    word="".join(word_remove_non_alpha)

    return word

def play_hangman(word):
    """
    Function to play the game
    """
    welcome()
    print("The word is " + word)

    word_completion = "_" * len(word) #length of chosen word
    guessed = False
    guessed_letters = []
    tries = 6

    print("Let's play Hangman!\n")
    print(f"Loading secret word from {category_name} category...")
    print("\n" + display_hangman(tries))
    print(word_completion)
    print("\n")

    while not guessed and tries > 0:
        guess = input("Please guess a letter and hit enter:\n").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"{Back.YELLOW+Style.BRIGHT}You already guessed the letter {guess}")
            elif guess not in word:
                print(f"{Fore.RED+Style.BRIGHT}{guess} is not in the word.")
                tries -= 1 #decrement the number of tries
                guessed_letters.append(guess)
            else:
                print(f"{Fore.GREEN+Style.BRIGHT}Well done! {guess} is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list) #convert back to a string

                #possible the guess now completes the word
                if "_" not in word_completion: 
                    guessed = True
        elif len(guess) > 1: #if user enters more than one letter at a time
            print("Sorry, only 1 letter at a time is allowed!")
        else:
            print("Not a valid guess. Only letters allowed!")
        print(f"{Fore.CYAN+Style.BRIGHT}Number of tries {tries}")
        print("\n" + display_hangman(tries) + "\n")
        print(word_completion)
        print("\n")
    
    if guessed: #if guess is True, player wins
        print(f"{Fore.GREEN+Style.BRIGHT}{WIN_ART}")
        print(f"{Back.GREEN}Congrats! You win!")
    else:
        print(f"{Fore.RED+Style.BRIGHT}{LOSE_ART}")
        print(f"{Back.RED+Style.BRIGHT}Sorry you ran out of tries.")
        print(f"\nThe word was {word}. Maybe next time.")

def main():
    """
    Run all program functions
    """
    main_menu()
    #welcome()
    #word = get_rand_word()
    #print("The word is " + word)
    #play_hangman(word)

main()