import gspread
from google.oauth2.service_account import Credentials
import random
import re

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSREAD_CLIENT.open('hangman')

print("Welcome to Hangman")
print("______________________________\n")

def get_rand_word():
    """
    Get random word from Google Sheets words list
    """
    words_sheet = SHEET.worksheet('words')
    words_list = words_sheet.get_all_values()
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

    word_completion = "_" * len(word) #length of chosen word
    guessed = False
    guessed_letters = []
    tries = 6

    print("Let's play Hangman!")
    print(word_completion)
    print("\n")

    while not guessed and tries > 0:
        guess = input("Please guess a letter and hit enter:\n").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1 #decrement the number of tries
                guessed_letters.append(guess)
            else:
                print("Well done!", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list) #convert back to a string

                #possible the guess now completes the word
                if "_" not in word_completion: 
                    guessed = True
        else:
            print("Not a valid guess.")
        print("Number of tries", tries)
        print(word_completion)
        print("\n")
    
    if guessed: #if guess is True, player wins
        print("Congrats! You win!")
    else:
        print("Sorry you ran out of tries. The word was " + word + ". Maybe next time.")

word = get_rand_word()
print("The word is " + word)
play_hangman(word)