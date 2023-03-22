import datetime
import os
import glob
import json
import random
import time

import bcrypt
import sqlite3
from pick import pick
from colorama import init as colorama_init, Fore as C, Style
from tabulate import tabulate
from rich.console import Console
from rich.markdown import Markdown
from Enums import QuizType

colorama_init(True)
DB_FILENAME: str = "data.db"
DB_DATE_FORMAT: str = "%Y-%m-%d %H:%M:%S"


def purge_all_users() -> bool:
    """
     Removes all files in the `users/` directory.
     :return: Whether the operation was executed(can be user cancelled)
     """

    files = glob.glob('./users/*')
    option, index = pick(["Yes", "No"], "Permanently remove all user data files? (Purges `./users/*` folder contents)",
                         indicator='🤔', default_index=1)
    if index == 0:
        for f in files:
            try:
                print(f"{C.RED}Removing {C.CYAN}{f}{C.RED} permanently.")
                os.remove(f)
            except Exception as e:
                print(f"{C.RED}Error while purging 	{C.BLUE}`users/`{C.RED} folder!")
                print(e)
                return False
    else:
        print("Cancelled operation.")
        return False


def get_user_save_data_path(username: str) -> str:
    """
    Get user file location
    :param username: player's username
    :return: file path as str
    """
    return f"users/{username}.json"


def check_if_user_data_present(user_name: str) -> bool:
    """
    Checks whether a user's save data file exists and is not empty.
    :param: user_name The user's name to look for
    :return: Whether the save data file was present in the `users/` directory.
     """
    # If the file exists
    if os.path.isfile(get_user_save_data_path(user_name)):
        with open(get_user_save_data_path(user_name), 'r') as f:
            # If it is not empty or whitespace/newline
            if len(f.read().strip()) != 0:
                f.close()
                return True
            f.close()
    return False


# --------------------------------
def doThing():
    title = 'Please choose an option from the menu (use arrow keys to navigate): '
    options = [purge_all_users.__name__, check_if_user_data_present.__name__,
               whitelist_user.__name__, backup_leaderboard.__name__,
               resetLeaderboard.__name__, un_whitelist_user.__name__,
               delete_account.__name__, change_admin_password.__name__,
               view_stats.__name__, create_default_db.__name__,
               "feedback", "exit",
               ]
    fb_options = [view_feedback.__name__, clear_feedback.__name__, "go back"]
    while True:
        option, index = pick(options, title, indicator='👉', default_index=1)

        match options[index]:
            case purge_all_users.__name__:
                purge_all_users()
            case check_if_user_data_present.__name__:
                username = input("Please enter the user's name to check for >> ")
                if check_if_user_data_present(username):
                    print(f"{C.GREEN}User data file {C.BLUE}{get_user_save_data_path(username)}{C.GREEN} exists!")
                else:
                    print(
                        f"{C.RED}User data file {C.BLUE}{get_user_save_data_path(username)}{C.RED} does {C.MAGENTA}NOT{C.RED} exist.")
            case whitelist_user.__name__:
                username = input("User to whitelist: ")
                whitelist_user(username)

            case resetLeaderboard.__name__:
                print("Reset leaderboard.")
                resetLeaderboard()
            case backup_leaderboard.__name__:
                print("Leaderboard backed up.")
                backup_leaderboard()
            case un_whitelist_user.__name__:
                un_whitelist_user(input("User to unwhitelist: "))
            case delete_account.__name__:
                delete_account(input("Account to delete: "))
                print("Account deleted.")
            case change_admin_password.__name__:
                change_admin_password(input("New password: "))
            case view_stats.__name__:
                view_stats()
            case "feedback":
                fb, fb_index = pick(fb_options, "Feedback", indicator="👉")
                match fb:
                    case view_feedback.__name__:
                        view_feedback()
                    case clear_feedback.__name__:
                        clear_feedback()
                        print("Feedback cleared.")
                    case "go back":
                        continue
            case "exit":
                exit()
            case _:
                print(f"No command was executed, {C.RED}something may be wrong with the menu code.{Style.RESET_ALL}")
                exit(1)
        input("Press enter to return to the administrative menu. ")


def whitelist_user(new_user) -> bool:
    """
    Whitelisted the user.
    :param: new_user The username to whitelist
    :return: Whether the user was whitelisted or not
    """
    with open("whitelist.json", "r") as w:
        whitelist = json.load(w)
    w.close()
    if not check_if_user_data_present(new_user):
        print("User does not exist.")
        return False
    elif new_user in whitelist:
        print("User is already whitelisted.")
        return False
    else:
        whitelist.append(new_user)
        with open("whitelist.json", "w") as w:
            json.dump(whitelist, w)
        print("Whitelisted " + new_user)
        return True


def un_whitelist_user(new_user):
    with open("whitelist.json", "r") as w:
        whitelist = json.load(w)
    w.close()
    if not check_if_user_data_present(new_user):
        print("User does not exist.")
        return False
    # if user is not in whitelist
    elif not new_user in whitelist:
        print("User is not whitelisted.")
        return False
    else:
        whitelist.remove(new_user)
        with open("whitelist.json", "w") as w:
            json.dump(whitelist, w)
        print("Un-whitelisted " + new_user)


def backup_leaderboard():
    with open("myfile.json", "r") as lb:
        lbd = json.load(lb)
    lb.close()
    with open("myfileBackup.json", "w") as lbb:
        json.dump(lbd, lbb)
    lbb.close()


def resetLeaderboard():
    with open("myfileBackup.json", "r") as lbb:
        lbd = json.load(lbb)
    lbb.close()
    with open("myfile.json", "w") as lb:
        json.dump(lbd, lb)
    lb.close()


def read_leaderboard(quiz_mode=None, alternate_question_type=None, num_questions=0):
    if num_questions == 3:
        num_questions = "threeq"
    elif num_questions == 10:
        num_questions = "tenq"
    elif num_questions == 20:
        num_questions = "twentyq"
    elif num_questions is None:
        pass
    else:
        num_questions = "threeq"

    with open("myfile.json", "r+") as lb_file:
        lb_data = json.load(lb_file)
        if quiz_mode == QuizType.EASY:
            quiz_mode = "Easy Mode"
        if quiz_mode == QuizType.NORMAL:
            quiz_mode = "Normal Mode"
        if quiz_mode == QuizType.HARD:
            quiz_mode = "Hard Mode"
        if quiz_mode == QuizType.QUICK:
            quiz_mode = "Quick Mode"
        if quiz_mode is None:
            quiz_mode = alternate_question_type
        times_in_min = []
        times_in_ms = []
        times_in_s = []
        names = []
        for mode in range(len(lb_data[f"{quiz_mode}, {num_questions}"].values())):
            mode = list(lb_data[f"{quiz_mode}, {num_questions}"].values())[mode][0]
            times_in_ms.append(int(mode % 1 * 100))
            times_in_s.append(int(mode // 1) % 60)
            times_in_min.append(int(mode // 60))
        for ms_ind in range(len(times_in_ms)):
            if len(str(times_in_ms[ms_ind])) == 1:
                times_in_ms[ms_ind] = f"0{times_in_ms[ms_ind]}"
            times_in_ms[ms_ind] = str(times_in_ms[ms_ind])
        for s_ind in range(len(times_in_s)):
            if len(str(times_in_s[s_ind])) == 1:
                times_in_s[s_ind] = f"0{times_in_s[s_ind]}"
            times_in_s[s_ind] = str(times_in_s[s_ind])
        for min_ind in range(len(times_in_min)):
            if len(str(times_in_min[min_ind])) == 1:
                times_in_min[min_ind] = f"0{times_in_min[min_ind]}"
            times_in_min[min_ind] = str(times_in_min[min_ind])
        for mode in range(len(lb_data[f"{quiz_mode}, {num_questions}"].values())):
            mode = list(lb_data[f"{quiz_mode}, {num_questions}"].values())[mode][1]
            names.append(mode)
        combined_times = []
        for i in range(3):
            combined_times.append(f"{times_in_min[i]}:{times_in_s[i]}:{times_in_ms[i]}")
        print_times = []
        combined = []
        for i in range(3):
            combined.append([combined_times[i], names[i]])
        print(tabulate(
            [time for time in combined],
            headers=["Time (min)", "Username"],
            tablefmt='orgtbl'
        ))
    lb_file.close()


def delete_account(username):
    username = str(username)
    if check_if_user_data_present(username):
        un_whitelist_user(username)
        os.remove(f"./users/{username}.json")


def give_info():
    options1 = ["Leaderboard", "Programmers", "Updates"]
    options11 = ["3 Questions", "10 Questions", "20 Questions"]
    options12 = ["Easy Mode", "Normal Mode", "Hard Mode", "Quick Mode"]
    options13 = ["Recent Updates", "Future Plans"]
    mmm, index1 = pick(options1, "What would you like info on?", indicator='👉', default_index=0)
    if index1 == 0:
        print("  					Info about leaderboard.", end="")
        print("""
        The leaderboard keeps track of the top three fastest times for getting every question correct. To qualify, you must not answer any questions wrong, and do so as quickly as possible. The categories are 3, 10 and 20 questions quick, easy, normal, or hard.
        """)

        view_leaderboard_choice: str = input("View leaderboard? (Y/n) >> ").lower()
        if view_leaderboard_choice == "y" or view_leaderboard_choice == "":
            mode11, index11 = pick(options11, "What leaderboard would you like to view?", indicator='👉',
                                   default_index=0)
            mode12, index12 = pick(options12, "What leaderboard would you like to view?", indicator='👉',
                                   default_index=0)
            match index11:
                case 0:
                    numQe = 3
                    pr = "Three Questions"
                case 1:
                    numQe = 10
                    pr = "Ten Questions"
                case 2:
                    numQe = 20
                    pr = "Twenty Questions"
            print("\t\t\t" + pr + ", " + mode12)
            read_leaderboard(num_questions=int(numQe), alternate_question_type=mode12)
        else:
            print("Exiting.")
            return

    if index1 == 1:
        print("  				Programmers Info")
        print("""
        This program was written by Unmesh Tokale and Sopan Jalkote, two high school students currently attending Round Rock
        High School in the 10th grade.
        """)
    if 2 == index1:
        # TODO: Move app flow to loops for each scene
        mmm, index13 = pick(options13, "What would you like info on? ", indicator='👉', default_index=0)
        if index13 == 0:
            print("  				Recent updates")
            print("""
            Recent updates have been focused on user-friendliness, including ensuring that non-numeric inputs do not raise errors. Learn Mode and basic features have also been implemented.
            """)
        if index13 == 1:
            with open('TODO.md', 'r') as todo_file:
                todo_markdown = todo_file.read()

                Console().print(Markdown(todo_markdown))
            todo_file.close()
    input("\nPress enter to return to the main menu\n")


def better_num_input(question_reprint: str = ""):
    while True:
        try:
            thing = input(question_reprint + "\n👉 ")
            if thing == "":
                eP = input("Exit program? Y/n ")
                if eP == "y" or eP == "":
                    print("Exited program")
                    exit()
                else:
                    print("Exit cancelled.")
                    continue
            int(thing)
            break
        except ValueError:
            print("Invalid input. ", end="")
    return thing


"""def betterNumInput(question_reprint: str = ""):
    did_int_parse_correctly = False
    while not did_int_parse_correctly:
        try:
            thing = input(question_reprint)
            int(thing)
            did_int_parse_correctly = True
        except ValueError:
            did_int_parse_correctly = False
            thing = input("Invalid input. " + question_reprint + "\n👉 ")
    return thing
"""


def better_frac_input(question_reprint, decimal=False):
    thing = input(question_reprint + "\n👉")
    state = True
    first = True
    num_dig = 0
    num_dot = 0
    num_slash = 0
    num_dash = 0
    empty_list = []
    skip_to_while_loop = False
    if thing == "":
        exit_choice = input("Exit program? Y/n ")
        if exit_choice == "y" or exit_choice == "":
            print(f"{C.YELLOW}Exited program")
            exit()
        else:
            print(f"{C.CYAN}Exit cancelled.")
            skip_to_while_loop = True
            state = False
    if not skip_to_while_loop:
        for i in thing:
            if first and i == "/":
                state = False

            if (not (i.isnumeric())) and (i != "/" or decimal) and i != "." and i != "-":
                state = False
            if i == ".":
                num_dot += 1
            if i == "/":
                num_slash += 1
            if i == "-":
                num_dash += 1
            first = False
            empty_list.append(i)
            num_dig += 1
        if (empty_list[0] == "." or empty_list[0] == "/" or empty_list[0] == "-") and num_dig == 1:
            state = False
        if num_dot > 1 or num_slash > 1 or num_dash > 1:
            state = False
        if num_dig == 2 and num_slash == 1:
            state = False
    while not state:
        dot_char = None
        first = True
        if not skip_to_while_loop:
            print("Invalid input. ", end="")
        thing = input(question_reprint + "\n👉 ")
        skip_to_while_loop = False
        if thing == "":
            exit_choice = input("Exit program? Y/n ")
            if exit_choice == "y" or exit_choice == "":
                print("Exited program")
                exit()
            else:
                print("Exit cancelled.")
                skip_to_while_loop = True
                continue
        state = True
        num_dig, num_dot, num_dash, num_slash = 0, 0, 0, 0
        empty_list = []
        for i in thing:
            if first and (i == "/"):
                state = False
            if (not (i.isnumeric())) and (i != "/" or decimal) and i != ".":
                state = False
            if i == ".":
                num_dot += 1
            if i == "/":
                num_slash += 1
            if i == "-":
                num_dash += 1
            first = False
            num_dig += 1
            empty_list.append(i)
        if (empty_list[0] == "." or empty_list[0] == "/" or empty_list[0] == "-") and num_dig == 1:
            state = False

        if num_dot > 1 or num_slash > 1 or num_dash > 1:
            state = False
        if num_dig == 2 and num_slash == 1:
            state = False

    return thing


def encrypt_password(password: str, return_as_str: bool = False):
    """Encrypts the given password (Should be str) and returns the result as either encoded or decoded."""
    bytes = password.encode('utf-8')  # encodes password str to an array of bytes
    hashed_pwd = bcrypt.hashpw(bytes, bcrypt.gensalt())  # Newly hashed & salted password
    if return_as_str:
        return hashed_pwd.decode('utf-8')
    return hashed_pwd


def check_password(user_pwd, retrieved_pwd) -> bool:
    # Check hashed password. Using bcrypt, the salt is saved into the hash itself
    user_pwd = user_pwd.encode("utf-8")
    if not type(retrieved_pwd) == bytes:
        retrieved_pwd = retrieved_pwd.encode("utf-8")
    return bcrypt.checkpw(user_pwd, retrieved_pwd)


def change_admin_password(new_pwd):
    new_pwd = encrypt_password(new_pwd, return_as_str=True)
    with open("adminpwd.json", "w+") as pF:
        json.dump(new_pwd, pF)
    print("Password changed successfully.")
    pF.close()


def gen_random_mode():
    modes = [QuizType.EASY, QuizType.NORMAL, QuizType.HARD, QuizType.QUICK]
    num_questions = [3, 10, 20]
    return random.choice(modes), random.choice(num_questions)


def log_feedback(username, feedback):
    with open("feedback.json", "r") as a_file:
        fb_data = json.load(a_file)
    a_file.close()
    state = False
    for thing in fb_data.keys():
        if username == thing:
            state = True
    if not state:
        fb_data[username] = []
    fb_data[username].append(feedback)
    with open("feedback.json", "w+") as a_file:
        json.dump(fb_data, a_file)


def clear_feedback():
    with open("feedback.json", "w") as a_file:
        json.dump({}, a_file)
    a_file.close()


def view_feedback():
    try:
        with open("feedback.json", "r") as a_file:
            fb_data = json.load(a_file)

        users = []
        for user in fb_data.keys():
            users.append(user)
        user_to_get_feedback, index = pick(users, "Feedback from which user?", indicator="👉")
        num_list = []
        for i in range(1, len(fb_data[user_to_get_feedback]) + 1):
            num_list.append(i)
        feedback_num, feedback_index = pick(num_list, "Which entry?", indicator="👉")
        print(fb_data[user_to_get_feedback][feedback_index])
    except ValueError:
        print("No feedback to be displayed at this moment.")


def delete_all_guests():
    files = glob.glob('./users/*')
    for file in files:
        if file.startswith("guest"):
            os.remove(file)


def log_stats(mode: QuizType):
    with open("statistics.json", "r+") as stats_file:
        statistics = json.load(stats_file)
    stats_file.close()
    statistics[f"{mode} Mode"] += 1
    with open("statistics.json", "w+") as stats_file:
        statistics = json.dump(statistics, stats_file)
    stats_file.close()


def view_stats():
    with open("statistics.json", "r+") as stats_file:
        statistics = json.load(stats_file)
    most_played_value = max(statistics.values())
    least_played_value = min(statistics.values())
    most_played_key = list(statistics.keys())[list(statistics.values()).index(most_played_value)]
    least_played_key = list(statistics.keys())[list(statistics.values()).index(least_played_value)]
    print(f"{most_played_key} is the most played mode with {most_played_value} plays.")
    print(f"{least_played_key} is the least played mode with {least_played_value} plays.")


# DATABASE STUFF —————————————————————————————————————————
def create_default_db():
    # Check if database file already exists
    if os.path.isfile(DB_FILENAME):
        print(f"{C.RED}Database file {C.CYAN}{DB_FILENAME}{C.RED} already exists.")
        return

    # Create & connect to the new database file
    conn = sqlite3.connect(DB_FILENAME)
    c = conn.cursor()

    # Create Users table
    c.execute('''CREATE TABLE Users
                 (username TEXT, password TEXT, account_creation_date TEXT)''')

    # Commit changes and close connection
    conn.commit()
    conn.close()

    print(f"{C.GREEN}Database file {C.CYAN}{DB_FILENAME}{C.GREEN} created successfully.")


# TODO: Use class to define data structure for the table!!! **Extremely important!**
def add_user_to_db(username: str, password: str, account_creation_date: datetime.date):
    # Connection to database
    conn = sqlite3.connect(DB_FILENAME)
    c = conn.cursor()

    # Convert date to format that sqlite likes
    account_creation_str: str = account_creation_date.strftime(DB_DATE_FORMAT)

    # Add row with user information
    c.execute("INSERT INTO Users VALUES (?, ?, ?)",
              (username, password, account_creation_str))

    # Commit changes
    conn.commit()

    # Get the ID of the last inserted row
    row_id = c.lastrowid

    # Fetch the corresponding row from the database
    c.execute("SELECT * FROM Users WHERE rowid = ?", (row_id,))
    row = c.fetchone()

    # Close the database connection
    conn.close()

    return row


def get_users_table_from_db():
    conn = sqlite3.connect(DB_FILENAME)
    c = conn.cursor()

    # Select all rows from Users table
    c.execute("SELECT * FROM Users")
    rows = c.fetchall()

    # Close connection
    conn.close()

    # Return the rows
    return rows
