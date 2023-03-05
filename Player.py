import json
import os
from datetime import datetime
from enum import Enum, unique

import re
import unicodedata
from colorama import init as colorama_init, Fore as C, Style
from tabulate import tabulate

import utils

colorama_init(True)


@unique  # Prevents overlap (Cannot be both EASY and HARD simultaneously)
class QuizType(Enum):
    def __str__(self):
        return str(self.value)

    EASY = "Easy"
    NORMAL = "Normal"
    HARD = "Hard"
    TWO_PLAYER_VS = "Two Player (v.s.)"


@unique  # Prevents overlap (Cannot be both EASY and HARD simultaneously)
class LeaderboardType(Enum):
    def __str__(self):
        match self.value:
            case 20:
                return "Twenty Question"
            case 10:
                return "Ten Question"
            case 3:
                return "Three Question"

    TWENTY_Q = 20
    TEN_Q = 10
    THREE_Q = 3


# SCORE CLASS –------------------------
class Score:
    def __init__(self, value: int, mode: QuizType, isHighScore: bool):
        self.value = value
        self.mode = mode
        self.isHighScore = isHighScore

    # def returnScoreInformation():
    #     return {}


# PLAYER CLASS –------------------------
class Player:

    @staticmethod
    def checkPassword(username: str, password: str):
        if utils.check_if_user_data_present(username):
            with open(f"users/{username}.json") as f:
                data = json.load(f)
                return password == data["password"]
        else:
            return False

    def __init__(self, name, mode, pwd=None, newAccount=False):
        """If the name is empty or whitespace, it will generate a guest username"""
        # Guest Username ------
        if name.isspace() or name == '':
            now = datetime.now()
            # guest_username: str = now.strftime("guest_%Y-%m-%d")
            guest_username: str = now.strftime("guest%s")
            print(f"{C.YELLOW}Empty username, setting to: {C.CYAN}{guest_username}")
            self.name: str = guest_username
        # Bad characters ------
        else:
            # Modified from https://github.com/django/django/blob/master/django/utils/text.py
            value = (
                unicodedata.normalize("NFKD", name)
                .encode("ascii", "ignore")
                .decode("ascii")
            )
            value = re.sub(r"[^\w\s-]", "", value.lower())
            value = re.sub(r"[-\s]+", "-", value).strip("-_")
            if name != value:
                print(f"{C.YELLOW}Bad characters removed, username is now {C.CYAN}{value}")
                self.name = value
            else:
                self.name = name
        # ---------------------
        self.score: int = 0
        self.num_correct: int = 0
        self.highscore: dict = {
            QuizType.EASY.value: 0,
            QuizType.NORMAL.value: 0,
            QuizType.HARD.value: 0
        }
        self.current_mode: QuizType = mode
        self._USER_DATA_FILE = f"users/{self.name}.json"
        self.password = pwd

        if newAccount:
            self.generateEmptyDataFile()
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
                print(f"{C.RED}No save data found! Creating basic data file: {C.CYAN}{self.generateEmptyDataFile()}")

    def generateEmptyDataFile(self) -> str:
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

    def calculateScore(self, total_questions: int) -> int:
        numWrong = total_questions - self.num_correct
        self.score = round(self.num_correct * 5 - numWrong * 4)
        return self.score

    def getNumStuff(self):
        return int(self.num_correct)

    def saveToScoreboard(self, quizmode):
        # Save the scoreboard to the user's file
        with open(self._USER_DATA_FILE, 'w+') as score_file:
            # IF THEY MADE A HIGH SCORE
            if self.score > self.highscore[quizmode.value]:
                self.highscore[quizmode.value] = self.score
                print(f"{C.LIGHTBLUE_EX}New High Score!!!!")
            json.dump({
                "name": self.name,
                "highscore": self.highscore,
                "password": self.password
            }, score_file)
        score_file.close()

    def changePassword(self, newPassword):
        with open(self._USER_DATA_FILE, 'r') as data_file:
            user_data = json.load(data_file)
            user_data['password'] = newPassword
        data_file.close()
        with open(self._USER_DATA_FILE, 'w') as data_file:
            data_file = json.dump(user_data, data_file)


# LEADERBOARD CLASS –------------------------
class Leaderboard:
    def __init__(self, mode: QuizType, numQuestions: int):
        self.numQuestions = numQuestions
        self.mode = mode

    def __str__(self):
        # TODO: Return a table using tabulate()
        pass