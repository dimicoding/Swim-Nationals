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
    print("Before you choose your races, I need some details...")
    print("Your Name, Year and Gender.\n")

    while True:
        #get users name and validate it
        print("Your name should contain between 3 and 9 letters.")
        print("Example: MichaelP\n")
        
        name= input("Enter your name here:\n")
        if name.isalpha() and len(name) > 2 and len(name) < 10:
            print("Hi! " + name + " what is the year you were born?")
            break
        else:
            print("Invalid name! Please enter a valid name.")
            
    while True:
        #get users birth year and validate it
        try:
            print("Type only the two last numbers.")
            print("Example: 00\n")
            year= input("Your year:\n")
            if year.isdigit() and len(year) ==2:
                year= int(year)
                print("Year valid.")
                break
            else:
                raise ValueError
        except ValueError:
                print("Invalid birth year, enter a valid year")  
    
    while True:
        #get users gender and validate it
        try:
            gender = input("Please enter your gender (M/F):\n")
            if gender.lower() not in ['m', 'f']:
                raise ValueError
            print("Recieving...")
            print(f'Verify if everythin is correct: name:"{name}"year:"{year}"gender:"{gender}')

            break
        except ValueError:
            print("Invalid gender. Please enter 'M' or 'F'.")
    


get_athlete_info()
