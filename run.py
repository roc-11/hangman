import gspread
from google.oauth2.service_account import Credentials
import random

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
print("______________________________")

def get_rand_word():
    """
    Get random word from Google Sheets words list
    """
    words_sheet = SHEET.worksheet('words')
    words_list = words_sheet.get_all_values()
    word = random.choice(words_list)
    return word

get_rand_word()