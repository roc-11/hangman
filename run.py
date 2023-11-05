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
     _______           _        _______  _______ 
    (  ____ )|\     /|( \      (  ____ \(  ____ /
    | (    )|| )   ( || (      | (    \/| (    \/
    | (____)|| |   | || |      | (__    | (_____ 
    |     __)| |   | || |      |  __)   (_____  )
    | (\ (   | |   | || |      | (            ) |
    | ) \ \__| (___) || (____/\| (____/\/\____) |
    |/   \__/(_______)(_______/(_______/\_______)
    """

WIN_ART = """
      
    ░██╗░░░░░░░██╗██╗███╗░░██╗███╗░░██╗███████╗██████╗░
    ░██║░░██╗░░██║██║████╗░██║████╗░██║██╔════╝██╔══██╗
    ░╚██╗████╗██╔╝██║██╔██╗██║██╔██╗██║█████╗░░██████╔╝
    ░░████╔═████║░██║██║╚████║██║╚████║██╔══╝░░██╔══██╗
    ░░╚██╔╝░╚██╔╝░██║██║░╚███║██║░╚███║███████╗██║░░██║
    ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝
    """

LOSE_ART = """
    
    ░██████╗░░█████╗░███╗░░░███╗███████╗  ░█████╗░██╗░░░██╗███████╗██████╗░
    ██╔════╝░██╔══██╗████╗░████║██╔════╝  ██╔══██╗██║░░░██║██╔════╝██╔══██╗
    ██║░░██╗░███████║██╔████╔██║█████╗░░  ██║░░██║╚██╗░██╔╝█████╗░░██████╔╝
    ██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░  ██║░░██║░╚████╔╝░██╔══╝░░██╔══██╗
    ╚██████╔╝██║░░██║██║░╚═╝░██║███████╗  ╚█████╔╝░░╚██╔╝░░███████╗██║░░██║
    ░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝  ░╚════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝
    """                                                                           

MENU_ART = '''

                           __________   ▄▄▄▄▄▄
                          | HELP ME! |  |    █
                           ¯¯¯¯¯¯¯¯¯¯\\  °    █            ▒▒▒▒▒▒▒▒
               █▄██▄█                  \\O/   █           ▒▒▌▒▒▐▒▒▌▒
      █▄█▄█▄█▄█▐█┼██▌█▄█▄█▄█▄█          |    █            ▒▀▄▒▌▄▀▒
      ███┼█████▐████▌█████┼███         / \\   █               ██
░░░░░░█████████▐████▌█████████░░░░░░████████████░░░░░░░░░░░░░██░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░By Róisín O'Connell░░░░░░
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
    ░░░░░░█████████▐████▌█████████░░░░░░████████████░░░░░░░░░░░░░██░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
        ''',
        # 5 head, torso, both arms, and one leg
        '''
                                            ▄▄▄▄▄▄
                                            |    █
                                            O    █            ▒▒▒▒▒▒▒▒
                █▄██▄█                     /|\\   █           ▒▒▌▒▒▐▒▒▌▒
        █▄█▄█▄█▄█▐█┼██▌█▄█▄█▄█▄█           /     █            ▒▀▄▒▌▄▀▒
        ███┼█████▐████▌█████┼███               █                 ██
    ░░░░░░█████████▐████▌█████████░░░░░░████████████░░░░░░░░░░░░░██░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
        ''',
        # 4 head, torso, and both arms
        '''
                                            ▄▄▄▄▄▄
                                            |    █
                                            O    █            ▒▒▒▒▒▒▒▒
                █▄██▄█                     /|\\   █           ▒▒▌▒▒▐▒▒▌▒
        █▄█▄█▄█▄█▐█┼██▌█▄█▄█▄█▄█               █             ▒▀▄▒▌▄▀▒
        ███┼█████▐████▌█████┼███               █                 ██
    ░░░░░░█████████▐████▌█████████░░░░░░████████████░░░░░░░░░░░░░██░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
        ''',
        # 3 head, torso, and one arm
        '''
                                            ▄▄▄▄▄▄
                                            |    █
                                            O    █            ▒▒▒▒▒▒▒▒
                █▄██▄█                     /|    █           ▒▒▌▒▒▐▒▒▌▒
        █▄█▄█▄█▄█▐█┼██▌█▄█▄█▄█▄█               █            ▒▀▄▒▌▄▀▒
        ███┼█████▐████▌█████┼███               █                 ██
    ░░░░░░█████████▐████▌█████████░░░░░░████████████░░░░░░░░░░░░░██░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
        ''',
        # 2 head and torso
        '''
                                            ▄▄▄▄▄▄
                                            |    █
                                            O    █            ▒▒▒▒▒▒▒▒
                █▄██▄█                     |    █           ▒▒▌▒▒▐▒▒▌▒
        █▄█▄█▄█▄█▐█┼██▌█▄█▄█▄█▄█               █            ▒▀▄▒▌▄▀▒
        ███┼█████▐████▌█████┼███               █                 ██
    ░░░░░░█████████▐████▌█████████░░░░░░████████████░░░░░░░░░░░░░██░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
        ''',
        # 1 head
        '''
                                            ▄▄▄▄▄▄
                                            |    █
                                            O    █            ▒▒▒▒▒▒▒▒
                █▄██▄█                          █           ▒▒▌▒▒▐▒▒▌▒
        █▄█▄█▄█▄█▐█┼██▌█▄█▄█▄█▄█               █            ▒▀▄▒▌▄▀▒
        ███┼█████▐████▌█████┼███               █                 ██
    ░░░░░░█████████▐████▌█████████░░░░░░████████████░░░░░░░░░░░░░██░░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
        ''',
        # 0 initial empty state
        '''
                                            ▄▄▄▄▄▄
                                            |    █
                                                █            ▒▒▒▒▒▒▒▒
                █▄██▄█                         █           ▒▒▌▒▒▐▒▒▌▒
        █▄█▄█▄█▄█▐█┼██▌█▄█▄█▄█▄█               █            ▒▀▄▒▌▄▀▒
        ███┼█████▐████▌█████┼███               █               ██
    ░░░░░░█████████▐████▌█████████░░░░░░████████████░░░░░░░░░░░░░██░░░░░░░░░
    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
        '''
    ]
    return stages[tries]

class Score():
    """
    A class to deal with scores in the Hangman game.
    """

    def __init__(self, player, wins):
        """ Initializes the Hangman score """
        self.player = player
        self.wins = wins

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
        time.sleep(3)
        main_menu()
    elif menu_options == '1':
        word = get_rand_word()
        welcome()
        play_hangman(word)
    elif menu_options == '2':
        show_instructions()
    elif menu_options == '3':
        #clear the terminal and exit the game
        print("______________________________\n")
        print("Thanks for visiting! See you next time.")
        print("Exiting game now...")
        time.sleep(4) #delay exit for 3 seconds to show message
        clear_terminal()
        exit()

def show_instructions():
    """
    Show user game instructions.
    User will access these by selecting "2" on main menu.
    """

    clear_terminal()

    print(RULES_ART)
    print(
        """
        This is a classic game of Hangman. Begin by pressing 1 on the main menu screen.
        First, choose a word category. The computer will then generate a random mystery 
        word from this category, with each letter shown as underscores (e.g. _ _ _ _ ). 
        The player must try to guess the word by typing one letter at a time.
        If the guess is correct, the letter will appear in the word.
        Each incorrect guess will cost you one of your 6 lives, and the 
        Hangman will start to be hanged! Once you run out of lives, the Hangman will 
        die and you will lose the game :(
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
    clear_terminal()
    global player_name
    print("______________________________\n")
    print(f"Loading category...\n")
    time.sleep(2) #2 second delay
    print(f"You have selected the category: {category_name} \n")
    print("______________________________\n")

    while True:
        player_name = input("Please enter your preferred game name:\n")
        #validate username
        if len(player_name) == 0 or player_name == "":
            print(f"{Back.BLUE+Style.BRIGHT}Sorry, you must enter a username!")
            continue
        elif not player_name.isalpha():
            print(f"{Back.BLUE+Style.BRIGHT}Sorry, your name must be letters ONLY!")
            continue
        else:
            return player_name

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
    
    print("CATEGORIES...\n")
    time.sleep(1.5)
    print("1. Countries")
    print("2. Sports")
    print("3. Zoo Animals")
    print("4. Fruit")
    print("5. Capital Cities (Europe)")
    print("6. Harry Potter")
    print("7. Pokémon")
    category = input("\nPlease select a category from the choices above: \n")

    valid_category = ["1", "2", "3", "4", "5", "6", "7"]
    words_sheet = SHEET.worksheet('words')
    #check category selection is valid
    if category not in valid_category:
        print(f"{Back.BLUE+Style.BRIGHT}Sorry, that is not a valid selection.")
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

def play_hangman_again():
    """
    Asks user if they would like to play Hangman again, by entering Y or N.
    Validate yes/no selection.
    """
    while True:
        play_again_choice = input("Would you like to play Hangman again? Enter Y or N: \n")
        if play_again_choice.upper() == "Y":
            clear_terminal()
            word = get_rand_word()
            play_hangman(word)
        elif play_again_choice.upper() == "N":
            main_menu()
        else:
            print(f"{Back.BLUE+Style.BRIGHT}Sorry, only Y or N is a valid response.")
            continue
            
def play_hangman(word):
    """
    Function to play the game
    """
    clear_terminal()
    
    print("______________________________\n")
    print(f"Greetings {player_name}! Glad to have you playing today!\n")

    #print("The word is " + word)

    word_completion = "_" * len(word) #length of chosen word
    guessed = False
    guessed_letters = []
    tries = 6

    print("Let's play Hangman!\n")
    print(f"Loading secret word from {category_name} category...")
    time.sleep(2) #2 second delay
    print("\n" + display_hangman(tries))
    print(word_completion)
    print("\n")

    while not guessed and tries > 0:
        guess = input("Please guess a letter and hit enter:\n").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"{Back.BLUE+Style.BRIGHT}You already guessed the letter {guess}")
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
            print(f"{Back.BLUE+Style.BRIGHT}Sorry, only 1 letter at a time is allowed!")
        else:
            print(f"{Back.BLUE+Style.BRIGHT}Not a valid guess. Only letters allowed!")
        print(f"{Fore.CYAN+Style.BRIGHT}Number of tries {tries}")
        print("\n" + display_hangman(tries) + "\n")
        print(word_completion)
        print("\n")
    
    if guessed: #if guess is True, player wins
        print(f"{Fore.GREEN+Style.BRIGHT}{WIN_ART}")
        print(f"{Fore.GREEN}Congrats {player_name}! You win! :) ")
        print(f"{Fore.GREEN}Woohoo...you saved the Hangman by guessing the word {word}!")
        play_hangman_again()
    else:
        print(f"{Fore.RED+Style.BRIGHT}{LOSE_ART}")
        print(f"{Fore.RED+Style.BRIGHT}Oh no! The Hangman has been hanged! :( ")
        print(f"{Fore.RED+Style.BRIGHT}Sorry {player_name}, you ran out of tries.")
        print(f"\nThe word was {word}. Maybe next time.")
        play_hangman_again()

def main():
    """
    Run all program functions
    """
    main_menu()

main()