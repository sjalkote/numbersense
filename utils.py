import os
import glob
from pick import pick
from colorama import init as colorama_init, Fore as C, Style

colorama_init(True)
import json
import getpass
import Player
from tabulate import tabulate
import bcrypt


def purge_all_users(overrideUserConfirmation: bool = True) -> bool:
    """
     Removes all files in the `users/` directory.
     :return: Whether the operation was executed (may be user cancelled)
     """

    files = glob.glob('./users/*')
    option, index = pick(["Yes", "No"], "Permanently remove all user data files? (Purges `./users/*` folder contents)",
                         indicator='🤔', default_index=1)
    if option == "Yes":
        for f in files:
            try:
                print(f)
                os.remove(f)
            except Exception as e:
                print(f"{C.RED}Error while purging 	{C.BLUE}`users/`{C.RED} folder!")
                print(e)
                return False
        with open("whitelist.json", "r") as w:
            data = json.load(w)
            for user in data:
                createDefault(user)
        return True

    else:
        print("Cancelled operation.")
        return False


def getUserSaveDataPath(username: str):
    return f"users/{username}.json"


def check_if_user_data_present(user_name: str) -> bool:
    """
     Checks whether a user's save data file exists and is not empty.
      :param: user_name The user's name to look for
    :return: Whether the save data file was present in the `users/` directory.
     """
    # If the file exists
    if os.path.isfile(getUserSaveDataPath(user_name)):
        with open(getUserSaveDataPath(user_name), 'r') as f:
            # If it is not empty or whitespace/newline
            if len(f.read().strip()) != 0:
                f.close()
                return True
            f.close()
    return False


def changePassword(player: Player, new_password: str):
    player.changePassword(new_password)


# --------------------------------
def doThing(player: Player):
    title = 'Please choose an option from the menu (use arrow keys to navigate): '
    options = [purge_all_users.__name__, check_if_user_data_present.__name__, changePassword.__name__,
               whitelistUser.__name__, backupLeaderboard.__name__, resetLeaderboard.__name__, createDefault.__name__,
               unwhitelistUser.__name__, deleteAccount.__name__]

    option, index = pick(options, title, indicator='👉', default_index=1)

    match options[index]:
        case purge_all_users.__name__:
            purge_all_users()
        case check_if_user_data_present.__name__:
            username = input("Please enter the user's name to check for >> ")
            if check_if_user_data_present(username):
                print(f"{C.GREEN}User data file {C.BLUE}{getUserSaveDataPath(username)}{C.GREEN} exists!")
            else:
                print(
                    f"{C.RED}User data file {C.BLUE}{getUserSaveDataPath(username)}{C.RED} does {C.MAGENTA}NOT{C.RED} exist.")
        case whitelistUser.__name__:
            username = input("User to whitelist: ")
            whitelistUser(username)
        case changePassword.__name__:
            new_password = getpass.getpass("Enter your new password: ")
            changePassword(player, new_password)
            print(f"{C.BLUE}Password changed, logging out...")
            exit(0)
        case resetLeaderboard.__name__:
            print("Reset leaderboard.")
            resetLeaderboard()
        case backupLeaderboard.__name__:
            print("Leaderboard backed up.")
            backupLeaderboard()
        case createDefault.__name__:
            inp = input("Enter name: ")
            createDefault(str(inp))
        case unwhitelistUser.__name__:
            unwhitelistUser(input("User to unwhitelist: "))
        case deleteAccount.__name__:
            deleteAccount(input("Account to delete: "))
        case _:
            print(f"No command was executed, {C.RED}something may be wrong with the menu code.{Style.RESET_ALL}")
            exit(1)


def whitelistUser(newUser):
    with open("whitelist.json", "r") as w:
        data = json.load(w)
    w.close()
    data.append(newUser)
    with open("whitelist.json", "w") as w:
        json.dump(data, w)
    print("Whitelisted " + newUser)


def unwhitelistUser(newUser):
    with open("whitelist.json", "r") as w:
        data = json.load(w)
    w.close()
    t = 0
    c = 0
    for i in data:
        if newUser == i:
            data.remove(newUser)
        else:
            c += 1
        t += 1
    if t == c:
        print("User is not whitelisted.")
        exit()
    with open("whitelist.json", "w") as w:
        json.dump(data, w)
    print("Unwhitelisted " + newUser)


def backupLeaderboard():
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


def createDefault(username):
    username = str(username)
    newPlayer: Player = Player.Player(username, None, "")
    return


def read_leaderboard(quiztype=None, altqtype=None, numQ=0):
    if numQ == 3:
        numQ = "threeq"
    elif numQ == 10:
        numQ = "tenq"
    elif numQ == 20:
        numQ = "twentyq"
    elif numQ == None:
        pass
    else:
        numQ = "threeq"

    with open("myfile.json", "r+") as lb_file:
        lb_data = json.load(lb_file)
        if quiztype == Player.QuizType.EASY:
            quiztype = "Easy Mode"
        if quiztype == Player.QuizType.NORMAL:
            quiztype = "Normal Mode"
        if quiztype == None:
            quiztype = altqtype

        print(tabulate(
            ([mode for mode in lb_data[f"{quiztype}, {numQ}"].values()]),
            headers=["Time", "Username"],
            tablefmt='orgtbl'
        ))
    lb_file.close()


def deleteAccount(username):
    username = str(username)
    if check_if_user_data_present(username):
        os.remove(f"./users/{username}.json")


def giveInfo():
    options1 = ["Leaderboard", "Programmers", "Updates"]
    options11 = ["3 Questions", "10 Questions", "20 Questions"]
    options12 = ["Easy Mode", "Normal Mode"]
    options13 = ["Recent Updates", "Future Plans"]
    mmm, index1 = pick(options1, "What would you like info on?", indicator='👉', default_index=0)
    if index1 == 0:
        print("  					Info about leaderboard.", end="")
        print("""
  	The leaderboard keeps track of the top three fastest times for getting every question correct. To qualify, you must not answer any questions wrong, and do so as quickly as possible. The categories are 3, 10 and 20 questions easy or hard.
  """)

        leaderboardInput: str = input("View leaderboard? (Y/n) >> ").lower()
        if leaderboardInput == "y" or leaderboardInput == "":
            mode11, index11 = pick(options11, "What leaderboard would you like to view?", indicator='👉',
                                   default_index=0)
            mode12, index12 = pick(options12, "What leaderboard would you like to view?", indicator='👉',
                                   default_index=0)
            match index11:
                case 0:
                    numQ = "threeq"
                    pr = "Three Questions"
                case 1:
                    numQ = "tenq"
                    pr = "Three Questions"
                case 2:
                    numQ = "twentyq"
                    pr = "Three Questions"
            print("\t\t\t" + pr + ", " + mode12)
            read_leaderboard(numQ=numQ, altqtype=mode12)
        else:
            print("Exiting.")
            return

    if index1 == 1:
        print("  				Programmers Info")
        print("""
  	This program was written by Unmesh Tokale and Sopan Jalkote, two high school students currently attending Round Rock High School in the 10th grade.
  """)
    if index1 == 2:
        # TODO: Move app flow to loops for each scene
        mmm, index13 = pick(options13, "What would you like info on? ", indicator='👉', default_index=0)
        if index13 == 0:
            print("  				Recent updates")
            print("""
	Recent updates have been focused on user-friendliness, including ensuring that non-numeric inputs do not raise errors. Learn Mode and basic features have also been implemented.
	  """)
        if index13 == 1:
            print("  				Future Plans")
            print("""
   	Coming Soon!
		- Large scale bug fixing!
  		- Replit DB!!!
	Future updates:
   		- 0.0.1b: Learn mode four groups, encryption
 		- 0.0.2: The decimal update! Coming mid-next week
   		- 0.2: Two-Player Mode!
   """)

    exit()


def betterNumInput(question_reprint: str = ""):
    did_int_parse_correctly = False
    while True:
        try:
            thing = input(question_reprint + "\n👉 ")
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


def betterFracInput(question_reprint, decimal=False):
    thing = input(question_reprint)
    state = True
    first = True
    emptyList = []
    for i in thing:
        if first and i == "/":
            state = False

        if (not (i.isnumeric())) and (i != "/" or decimal) and i != "." and i != "-":
            state = False
        first = False
        emptyList.append(i)
    if emptyList[0] == ".":
        state = False
    while not state:
        first = True
        thing = input("Invalid input. " + question_reprint + "\n👉 ")
        state = True
        numDig = 0
        for i in thing:
            if first and (i == "/"):
                state = False
            if (not (i.isnumeric())) and (i != "/" or decimal) and i != ".":
                state = False
            first = False
            numDig += 1

        if (emptyList[0] == "." or emptyList[0] == "/") and numDig == 1:
            state = False
    return thing


def encrypt(password):
    password = password.encode("UTF-8")
    return bcrypt.hashpw(password, bcrypt.gensalt())