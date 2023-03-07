import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint
import colorama
from colorama import Fore, Back, Style


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
sh = GSPREAD_CLIENT.open('Swim_Nationals')

colorama.init()


def users_name():
    """
    get the name from the input
    get users name and birth year.
    Run a while loop to collect valid data.
    Name, must be between 2 and 10letters.
    """
    print("Before you choose your races, I need some details: ")
    print("Let's start with your Name.\n")

    global name
    while True:

        print("Your name, should contain between 3 and 9 letters.")
        print("Example: MichaelP\n")

        name = input("Enter your name here:\n")
        if name.isalpha() and len(name) > 2 and len(name) < 10:
            print("")
            print("Hi " + name + "!\n")
            break
        else:
            print("Invalid name! Please enter a valid name.")
    return name


def users_year():
    """
    get the birth year from the input
    Run a while loop to collect valid data.
    Last two numbers of birth the birth year.
    """
    global year
    while True:

        try:
            print("What is your birth year?")
            print("Type only the two last numbers.")
            print("Example: 91\n")
            year = input("Your year:\n")
            if year.isdigit() and len(year) == 2:
                year = int(year)
                print("")
                print("Good job.")
                print("The list of swimming events available")
                print("in the national competition is as follows.")
                print("You may choose one event for now.\n")
                break
            else:
                raise ValueError
        except ValueError:
            print("Invalid birth year, enter a valid year")
    return year


def events():
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
    print("")

    global user_distance
    while True:
        '#get users distance and validate it'
        print("Distance of your stroke, must be a number. Example:'200'")
        try:
            user_distance = input("Insert your distance here:  \n")
            if user_distance.isdigit() and len(user_distance) < 5:
                print("")
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
            cell = worksheet.cell(row_index + 1,
                   3 if gender.upper() == "M" else 4)
            time = cell.value
            '#colors, yellow_start/yellow_finish'
            y_s = Fore.YELLOW + Style.BRIGHT
            y_f = Fore.RESET + Style.RESET_ALL
            b_s = Fore.BLUE
            b_f = Fore.RESET
            print(
                y_s + "To qualify for" + y_f + b_s + f" {user_distance}m" +
                f" {user_stroke}, " + b_f + y_s + "gender " +
                y_f + b_s + f"({gender})" + b_f + y_s +
                " you need to swim faster than" + y_f +
                b_s + f" {time}s." + b_f
                )
            print("")
            break

        else:
            print("Error: Combination of stroke and distance is not valid...")
            return get_quali_time()


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
    should_repeat = True
    while should_repeat:
        users_name()
        users_year()
        events()
        get_quali_time()
        append_to_sheet(name, year, user_stroke, user_distance, gender)
        while True:
            """
            Create an option to the user:
            - Either continue to choosing another event
            - Exit the program
            """
            try:
                print("Select another race?")
                repeat = input("Type: (Y/N):  \n")
                if repeat.upper() == "Y":
                    print("Redirecting...")
                    break
                elif repeat.upper() == "N":
                    print("")
                    print("Thank you for using the program.\n"
                          "Hope to see you again soon!")
                    should_repeat = False
                    break
                else:
                    raise ValueError("Error: The letter is not attributed...")
            except ValueError as e:
                print(e)


print("\n")
print(Fore.YELLOW + Style.BRIGHT + "                        SWIM" +
      Back.RESET + Fore.RESET + Style.RESET_ALL + "-" +
      Fore.BLUE + Style.BRIGHT + "NATIONALS\n" + Fore.RESET + Style.RESET_ALL)

main()
