import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
CREDS= Credentials.from_service_account_file('creds.json')
SCOPED_CREDS= CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT= gspread.authorize(SCOPED_CREDS)
sh= GSPREAD_CLIENT.open('Swim_Nationals')


def get_athlete_info():
    """
    get users name, age and gender.
    Run a while loop to collect valid data.
    Name, must be between 2 and 10letters.
    Age, last two numbers of birth the birth year.
    Gender, either "m" or "f" letter.
    """
    while True:
        print("Before you choose your races, I need some details...")
        print("Your Name, Year and Gender.\n")
        
        print("Your name should contain between 3 and 9 letters.")
        print("Example: Michael P\n")

        name= input("Enter your name here:\n")
        if name.isalpha(len(name) > 2 and len(name) < 10):
            print("Hi! " + name + " what is the year you were born?")
            
        else:
            raise ValueError("Invalid name! Please enter a valid name.")
            break

        print("Type only the two last numbers.")
        print("Example: 00\n")
        year= int(input("Your year:\n"))
        


        
            



        break



get_athlete_info()
