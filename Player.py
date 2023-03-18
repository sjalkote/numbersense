import json
import os
from datetime import datetime
from enum import Enum, unique

import re
import unicodedata
from colorama import init as colorama_init, Fore as C, Style
from tabulate import tabulate
from getpass import getpass
from Enums import QuizType

import utils

colorama_init(True)


# PLAYER CLASS –------------------------
class Player:
    @staticmethod
    def fix_username(username: str) -> str:
        corrected_username: str = ''
        # Guest Username ------
        if username.isspace() or username == '':
            now = datetime.now()
            # guest_username: str = now.strftime("guest_%Y-%m-%d")
            guest_username: str = now.strftime("guest%s")
            print(f"{C.YELLOW}Empty username, setting to: {C.CYAN}{guest_username}")
            corrected_username: str = guest_username
        # Bad characters ------
        else:
            # Modified from https://github.com/django/django/blob/master/django/utils/text.py
            value = (
                unicodedata.normalize("NFKD", username)
                .encode("ascii", "ignore")
                .decode("ascii")
            )
            # Commented this line to allow upper and lower case
            value = re.sub(r"[^\w\s-]", "", value)
            value = re.sub(r"[-\s]+", "-", value).strip("-_")
            if username != value:
                # print(f"{C.YELLOW}Bad characters removed, username is now {C.CYAN}{value}")
                corrected_username = value
            else:
                corrected_username = username
        return corrected_username

    @staticmethod
    def checkPassword(username: str, provided_password: str) -> bool:
        try:
            with open(f"users/{username}.json") as f:
                data = json.load(f)
                return utils.check_password(provided_password, data["password"])
        except FileNotFoundError:
            print(f"{C.RED}Couldn't find player data for {C.BLUE}{username}{C.RED} when checking password.")
        return False

    def __init__(self, username, mode, password=None):
        """If the name is empty or whitespace, it will generate a guest username"""
        # USERNAME HANDLING ----------------------------------------------------
        new_account = False
        self.name = self.fix_username(username)
        if self.name != username:
            print(f"{C.YELLOW}Bad characters removed, username is now {C.CYAN}{self.name}")

        # ACCOUNT LOGIN / CREATION ----------------------------------------------------

        # Entering Password ---------------
        if utils.check_if_user_data_present(
                username):  # Check to make sure a user with this name does not already exist
            tries: int = 0
            login_successful: bool = False
            while not login_successful:
                tries += 1  # Because you start on the first try
                # Max no. of tries is 3
                if tries > 3:
                    print(f"{C.RED}Max tries reached, exiting...")
                    exit()

                password = getpass()
                if Player.checkPassword(username, password):
                    print(f"{C.GREEN}Correct password.{Style.RESET_ALL} Welcome back, {C.MAGENTA}{username}")
                    login_successful = True
                else:
                    print(
                        f"{C.RED}Incorrect password.{Style.RESET_ALL} Try again ({C.YELLOW}{tries}/3 tries{Style.RESET_ALL})")
        else:
            password = getpass("Enter new password for this account: ")
            new_account = True
        # --------------------------------------------------------------------------------------------------------
        self.score: int = 0
        self.num_correct: int = 0
        self.highscore: dict = {
            QuizType.EASY.value: 0,
            QuizType.NORMAL.value: 0,
            QuizType.HARD.value: 0,
            QuizType.QUICK.value: 0
        }
        self.current_mode: QuizType = mode
        self._USER_DATA_FILE = f"users/{self.name}.json"
        self.password: str = utils.encrypt_password(password, True)  # Hashed password as str

        if new_account:
            self.generate_empty_data_file()
        else:
            # Load data if exists
            os.makedirs(os.path.dirname(self._USER_DATA_FILE), exist_ok=True)
            if os.path.isfile(self._USER_DATA_FILE) and os.stat(self._USER_DATA_FILE).st_size != 0:
                with open(self._USER_DATA_FILE, "r") as score_file:
                    player_data = json.load(score_file)
                    try:
                        self.password = player_data["password"]
                        # If the key is not yet in the file (e.g. no HARD value, it will add it)
                        self.highscore.update(player_data['highscore'])
                        print(f"{C.GREEN}Retrieved High Scores!{Style.RESET_ALL}")
                        print(tabulate([
                            [score for score in self.highscore.values()]
                        ],
                            headers=[mode for mode in self.highscore.keys()],
                            tablefmt='orgtbl'))

                    except KeyError:
                        pass
                score_file.close()
            else:
                print(f"{C.RED}No save data found! Creating basic data file: {C.CYAN}{self.generate_empty_data_file()}")

    def get_high_scores(self):
        with open(self._USER_DATA_FILE, "r") as score_file:
            player_data = json.load(score_file)
            try:
                self.password = player_data["password"]
                # If the key is not yet in the file (e.g. no HARD value, it will add it)
                self.highscore.update(player_data['highscore'])
                print(f"{C.GREEN}Retrieved High Scores!{Style.RESET_ALL}")
                print(tabulate([
                    [score for score in self.highscore.values()]
                ],
                    headers=[mode for mode in self.highscore.keys()],
                    tablefmt='orgtbl'))

            except KeyError:
                pass

    def generate_empty_data_file(self) -> str:
        with open(self._USER_DATA_FILE, "w+") as data_file:
            self.password = self.password
            json.dump({
                "name": self.name,
                "highscore": self.highscore,
                "password": self.password
            }, data_file)
        data_file.close()
        return self._USER_DATA_FILE

    def __str__(self):
        return str(self.name)

    def calculate_score(self, total_questions: int) -> int:
        num_wrong = total_questions - self.num_correct
        self.score = round(self.num_correct * 5 - num_wrong * 4)
        return self.score

    def get_nem_stuff(self):
        return int(self.num_correct)

    def save_to_scoreboard(self, quiz_mode):
        # Save the scoreboard to the user's file
        with open(self._USER_DATA_FILE, 'w+') as score_file:
            # IF THEY MADE A HIGH SCORE
            if self.score > self.highscore[quiz_mode.value]:
                self.highscore[quiz_mode.value] = self.score
                print(f"{C.LIGHTBLUE_EX}New High Score!!!!")
            json.dump({
                "name": self.name,
                "highscore": self.highscore,
                "password": self.password
            }, score_file)
        score_file.close()

    def changePassword(self, new_password):
        with open(self._USER_DATA_FILE, 'r') as data_file:
            user_data = json.load(data_file)
            new_password = utils.encrypt_password(new_password, return_as_str=True)
            user_data['password'] = new_password
        data_file.close()
        with open(self._USER_DATA_FILE, 'w') as data_file:
            json.dump(user_data, data_file)

# LEADERBOARD CLASS –------------------------
