import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
sh = GSPREAD_CLIENT.open('Swim_Nationals')


"""
get users name, age and gender.
Run a while loop to collect valid data.
Name, must be between 2 and 10letters.
Age, last two numbers of birth the birth year.
Gender, either "m" or "f" letter.
"""

print("Before you choose your races, I need some details...")
print("Your Name, and Year of birth.\n")


def users_name():
    """
    get the name from the input
    """
    global name
    while True:
        """
        get users name and validate it
        """
        print("Your name should contain between 3 and 9 letters.")
        print("Example: MichaelP\n")

        name = input("Enter your name here:\n")
        if name.isalpha() and len(name) > 2 and len(name) < 10:
            print("Hi! " + name + " what is the year you were born?")
            break
        else:
            print("Invalid name! Please enter a valid name.")
    return name


def users_year():
    """
    get the birth year from the input
    """
    global year
    while True:
        """
        get users birth year and validate it
        """

        try:
            print("Type only the two last numbers.")
            print("Example: 00\n")
            year = input("Your year:\n")
            if year.isdigit() and len(year) == 2:
                year = int(year)
                print("Year valid.")
                break
            else:
                raise ValueError
        except ValueError:
            print("Invalid birth year, enter a valid year")
    return year


def Events():
    """
    Just prints the distances and srokes to the user in a ordered way.
    """
    events = {
        50:  ["free", "fly", "back", "breast"],
        100: ["free", "fly", "back", "breast"],
        200: ["free", "fly", "back", "breast", "medley"],
        400: ["free", "medley"],
        800: ["free"],
        1500: ["free"],
        }

    pprint(events)


def get_quali_time():
    """
    define lists for stroke, distance and gender
    iterate trought each of them and get a time stored in a specified cell
    """
    worksheet = sh.worksheet('Events')

    '#access columns in the sheet'
    strokes = worksheet.col_values(1)
    distances = worksheet.col_values(2)
    m_times = worksheet.col_values(3)
    f_times = worksheet.col_values(4)
    print("")

    global user_stroke
    print("Which stroke you want to swim, for example:'medley'")
    user_stroke = input("Insert your stroke here:  \n")

    global user_distance
    while True:
        '#get users distance and validate it'
        print("Distance of your stroke, must be a number for example:'200'")
        try:
            user_distance = input("Insert your distance here:  \n")
            if user_distance.isdigit() and len(user_distance) < 5:
                print("Distance is valid!")
            else:
                raise ValueError
            break
        except ValueError:
            print("Error: enter a number from 50 to 1500.")

    global gender
    while True:
        '#get users gender and validate it'
        print("Select the gender you're competing in, for example 'M' or 'F'")
        try:
            gender = input("Insert your gender here:  \n")
            if gender.upper() in ("M", "F"):
                print("Recieving...\n")
            else:
                raise ValueError
            break
        except ValueError:
            print("Error: Invalid gender.")

    while True:
        '#iterate torught strokes/distances'
        row_index = -1
        for i in range(len(strokes)):
            if strokes[i] == user_stroke and distances[i] == user_distance:
                row_index = i
                if gender.upper() == "M":
                    time = m_times[i]
                else:
                    time = f_times[i]
                break

            # access the cell containing the time and print its value
        if row_index >= 0:
            cell = worksheet.cell(row_index + 1 ,3 if gender.upper() == "M" else 4)
            time = cell.value
            print(f"To qualify for {user_distance}m {user_stroke} ({gender})")
            print(f"you need to swim faster than {time}s.\n")
            break

        else:
            print("Error: Combination of stroke and distance is not valid...")
            return get_quali_time()


def whats_next():
    """
    Create an option to the user:
     - Either continue to choosing another event
     - Exit the program
    """
    print("What would you like to do next?")
    while True:
        try:
            print("Select another race?")
            repeat = input("Type: 'Y' or 'N':  \n")
            if repeat.upper() == "Y":
                print("redirecting...")
                break
            elif repeat.upper() == "N":
                print("Plasure, see you next time)")
                break
            else:
                raise ValueError("Error: The letter is not attributed...")
        except ValueError as e:
            print(e)


def append_to_sheet(name, year, user_stroke, user_distance, gender):
    """
    Print the users stroke to the sheet
    """
    worksheet = sh.worksheet('Athlete')
    row = [name, year, user_stroke, user_distance, gender]
    worksheet.append_row(row)


def main():
    global name
    global year
    global user_stroke
    global user_distance
    global gender
    while True:
        users_name()
        users_year()
        Events()
        get_quali_time()
        whats_next()
        append_to_sheet(name, year, user_stroke, user_distance, gender)
        repeat = input("Do you want to continue? (Y/N)")
        if repeat.upper() == "N":
            print("Exiting program...")
            break


main()
