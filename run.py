import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

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
        '#get users gender and validate it'
        try:
            gender = input("Please enter your gender (M/F):\n")
            if gender.lower() not in ['m', 'f']:
                raise ValueError
            print("Recieving...")
            print(f'Verify if everything is correct:\
                   "name:"{name}" year: "{year}" gender: "{gender} ')

            break
        except ValueError:
            print("Invalid gender. Please enter 'M' or 'F'.")


def Events():
    """
    Just prints the distances and srokes to the user in a ordered way.
    """
    events = {
        50:["Free", "Fly", "Back", "Breast"],
        100:["Free", "Fly", "Back", "Breast"],
        200:["Free", "Fly", "Back", "Breast", "IM"],
        400:["Free", "IM"],
        800:["Free"],
        1500:["Free"],
        }

    pprint(events)


def get_quali_time():
    """
    define lists for stroke, distance and gender
    iterate trought each of them and get a time stored in a specified cell
    """
    worksheet = sh.worksheet('Events')
    
    #access columns in the sheet
    strokes= worksheet.col_values(1)
    distances= worksheet.col_values(2)
    m_times= worksheet.col_values(3)
    f_times= worksheet.col_values(4)
    print("")
    user_stroke= input("pick a stroke:")
    user_distance=input("pick a distance:")
    user_gender= input("M or F:")

    row_index = -1
    for i in range(len(strokes)):
        if strokes[i] == user_stroke and distances[i] == user_distance:
            row_index = i
            if user_gender == "M":
                time = m_times[i]
            else:
                time = f_times[i]
            break
    
    # access the cell containing the time and print its value
    if row_index >= 0:
        cell = worksheet.cell(row_index + 1, 3 if user_gender == "M" else 4)
        time = cell.value
        print(f"The qualifying time for {user_stroke} {user_distance} ({user_gender}) is {time}.")
    else:
        print("Error: combination of stroke, distance, and gender not found.")






def main():
    personal_info= get_athlete_info()
    races= Events()
    times= get_quali_time()



""""
for user_stroke in strokes:
        for user_distances in distances:
            for user_gender in m_times:
                time = worksheet.cell().value
                print(time)
"""


















"""
print("Finally let's choose a race")
distance= input("Select your distance:\n")
stroke= input("Select your stroke:\n")
self.selected_races=[]

def choose_races(self, races):
    if races in self.events_dict:
        self.selected_races.append(races)
    else:
        print("Race not Valid")


records_data = sh.worksheet("Events").get_all_records()
pprint(records_data)

def pick_races():

    #- Create a loop which will allow the user to pick the races
    #- The choices should be printed out to the excel file

    while True:
        input()
    

worksheet = sh.worksheet('Events')
value= worksheet.acell('C2').value
print(value)
"""