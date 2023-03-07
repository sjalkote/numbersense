# Link to practice test: http://bryantheath.com/files/2018/03/Q061.pdf
import random
import questions
import time
import json
from Player import Player, QuizType
from colorama import init as colorama_init, Fore as C, Style, ansi
from pick import pick
import utils
import learnmode as lm

from rich.console import Console
from rich.markdown import Markdown

# TESTING -----------------------
MARKDOWN = """
## Numbersense.py

[GitHub Page](https://github.com/TechnoShip123/numbersense)

"""

console = Console().print(Markdown(MARKDOWN))

# -------------------------------
colorama_init(True)


def write_leaderboard(quiztype: QuizType, player1: Player, total, time_lapsed):
    numC = float(player1.getNumStuff())
    if numC / float(total) == 1.0:
        datae = displayLeaderboard(quizMode, time=time_lapsed, numQuestions=total, player=player1)
    else:
        datae = displayLeaderboard(quizMode)
    with open('myfile.json', 'w') as leaderboard_file:
        json.dump(datae, leaderboard_file)
    leaderboard_file.close()


def time_convert(sec):
    sec = round(sec)
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    print("Time Lapsed = {:02d}:{:02d}:{:02d}".format(int(hours), int(mins), sec))


global player1


def main(totalQuestions: int, player1: Player):
    # TODO: @pikadabber24 This is not being used for some reason something must be wrong !!!!!!!!!!!!!!!!
    counter = 1

    while counter <= totalQuestions:
        if player1.current_mode == QuizType.NORMAL:
            print(f"{counter}) ", end="")
            questionType = random.randint(1, 26)
            # Print the question number
            match questionType:
                case 1:
                    if questions.divideBy(random.randint(1, 25)):
                        player1.num_correct += 1
                case 2:
                    if questions.multiplyBy():
                        player1.num_correct += 1
                case 3:
                    if questions.multiplyFractions():
                        player1.num_correct += 1
                case 4:
                    if questions.centeredAroundThird():
                        player1.num_correct += 1
                case 5:
                    if questions.squareNumber():
                        player1.num_correct += 1
                case 6:
                    if questions.cubeNumber():
                        player1.num_correct += 1
                case 7:
                    if questions.squareRootNumber():
                        player1.num_correct += 1
                case 8:
                    if questions.cubeRootNumber():
                        player1.num_correct += 1
                case 9:
                    if questions.differenceOfReverses(random.randint(3, 4)):
                        player1.num_correct += 1
                case 10:
                    if questions.gcflcmQuestion():
                        player1.num_correct += 1
                case 11:
                    if questions.addSquares(random.randint(1, 2)):
                        player1.num_correct += 1
                case 12:
                    if questions.remainder():
                        player1.num_correct += 1
                case 13:
                    if questions.compareFractions():
                        player1.num_correct += 1
                case 14:
                    if questions.differenceOfSquares():
                        player1.num_correct += 1
                case 15:
                    if questions.closeToHundred():
                        player1.num_correct += 1
                case 16:
                    if questions.xAndyCubed():
                        player1.num_correct += 1
                case 17:
                    if questions.divideFractions():
                        player1.num_correct += 1
                case 18:
                    if questions.stats():
                        player1.num_correct += 1
                case 19:
                    if questions.integralDivisorsQuestion():
                        player1.num_correct += 1
                case 20:
                    if questions.logarithmQuestion():
                        player1.num_correct += 1
                case 21:
                    if questions.sepDigits():
                        player1.num_correct += 1
                case 22:
                    if questions.xtoy1():
                        player1.num_correct += 1
                case 23:
                    if questions.addCommonProducts():
                        player1.num_correct += 1
                case 24:
                    if questions.subsetsQuestion():
                        player1.num_correct += 1
                case 25:
                    if questions.multiplyOver37():
                        player1.num_correct += 1
                case 26:
                    if questions.orderOfOperationsQuestion():
                        player1.num_correct += 1

            counter += 1

        elif player1.current_mode == quizMode.EASY:
            QuestionType = random.randint(1, 6)
            print(f"{counter}) ", end="")
            match QuestionType:
                case 1:
                    if questions.divideBy(random.randint(1, 10)):
                        player1.num_correct += 1
                case 2:
                    if questions.multiplyBy():
                        player1.num_correct += 1
                case 3:
                    if questions.multiplyFractions():
                        player1.num_correct += 1
                case 4:
                    if questions.squareNumber(easy=True):
                        player1.num_correct += 1
                case 5:
                    if questions.addSquares(1):
                        player1.num_correct += 1
                case 6:
                    if questions.gcflcmQuestion():
                        player1.num_correct += 1
            counter += 1
        else:
            print("Error #0: Not found")
            exit()
    print(f"Questions answered correctly: {player1.num_correct}/{totalQuestions}")
    return totalQuestions


def displayLeaderboard(mode: QuizType, time=None, numQuestions=None, player=None):
    # start of where error could occur

    if time != None:
        time = int(round(time, 0))
    if numQuestions != None:
        numQ = int(numQuestions)

    with open("myfile.json", "r+") as data_file:
        data = json.load(data_file)

    # end
    data_file.close()
    if time == None:
        return data
    if numQuestions == None:
        return data

    # 20 questions
    # TODO: we shouldn't need this since we implemented __str__() method for the enum
    match mode:
        case QuizType.NORMAL:
            mode = "Normal Mode"
        case QuizType.EASY:
            mode = "Easy Mode"

    if numQ != 3 and numQ != 10 and numQ != 20:
        return data

    match numQ:
        case 3:
            numQ = "threeq"
            pnumQ = "Three Questions"
        case 10:
            numQ = "tenq"
            pnumQ = "Ten Questions"
        case 20:
            numQ = "twentyq"
            pnumQ = "Twenty Questions"

    if time < int(data[f"{mode}, {numQ}"]["First"][0]):
        print(f"Congratulations! You made First Place in {pnumQ}, {mode}")
        data[f"{mode}, {numQ}"]["Third"][0], data[f"{mode}, {numQ}"]["Third"][1] = data[f"{mode}, {numQ}"]["Second"][0], \
                                                                                   data[f"{mode}, {numQ}"]["Second"][1]
        data[f"{mode}, {numQ}"]["Second"][0], data[f"{mode}, {numQ}"]["Second"][1] = data[f"{mode}, {numQ}"]["First"][
                                                                                         0], \
                                                                                     data[f"{mode}, {numQ}"]["First"][1]
        data[f"{mode}, {numQ}"]["First"][0], data[f"{mode}, {numQ}"]["First"][1] = time, str(player1)

    elif time < int(data[f"{mode}, {numQ}"]["Second"][0]):
        print(f"Congratulations! You made Second Place in {pnumQ}, {mode}")
        data[f"{mode}, {numQ}"]["Third"][0], data[f"{mode}, {numQ}"]["Third"][1] = data[f"{mode}, {numQ}"]["Second"][0], \
                                                                                   data[f"{mode}, {numQ}"]["Second"][1]
        data[f"{mode}, {numQ}"]["Second"][0], data[f"{mode}, {numQ}"]["Second"][1] = time, str(player1)

    elif time < int(data[f"{mode}, {numQ}"]["Third"][0]):
        print(f"Congratulations! You made Third Place in {pnumQ}, {mode}")
        data[f"{mode}, {numQ}"]["Third"][0], data[f"{mode}, {numQ}"]["Third"][1] = time, str(player1)

    return data


# Make sure this is the main file ------------------------------
if __name__ == "__main__":
	# Get the quiz mode
	
	quizMode: QuizType = None
	# Whether we should generate basic user data file instantly
	# TODO: This will later be replaced by adding a new row with default info to database
	newAccount: bool = False
	print(ansi.BEL, end='')
	username = input("Username: ")
	
	# Entering Password ---------------
	if utils.check_if_user_data_present(username):
		tries: int = 0
		loginSuccessful: bool = False
		while not loginSuccessful:
			tries += 1  # Because you start on the first try
			# Max no. of tries is 3
			if tries > 3:
				print(f"{C.RED}Max tries reached, exiting...")
				exit()
	
			password = input("Password: ")
			if Player.checkPassword(username, password):
				print(f"{C.GREEN}Correct password.{Style.RESET_ALL} Welcome back, {C.MAGENTA}{username}")
				loginSuccessful = True
			else:
				print(
					f"{C.RED}Incorrect password.{Style.RESET_ALL} Try again ({C.YELLOW}{tries}/3 tries{Style.RESET_ALL})")
	else:
		password = input("Enter new password for this account: ")
		newAccount = True
	
	# ----------------------------------------------------
	while True:
		title = 'Choose a quiz mode: '
		options = ["😀 Easy", "😐 Normal", "👺 Hard", "🤝 2 Player (v.s.)", "⚙️ Settings", "🔒 Administrative Menu",
				   "📙 Learn Mode", "Exit"]
		settingsOptions = ["🔑 Change Password", "❌ Delete Account", "📄 Get additional Info"]
		lmGroups = ["Multiplying, Dividing, and Fractions", "Powers", "Addition and Subtraction"]
		lmGroupsOne = ["Multiplying by 25", "Multiplying by 75", "Multiplying by 101", "Multiplying by 11",
					   "Multiplying Fractions", "Multiplying Two Numbers Centered Around a Third", "Remainders",
					   "Compare Fractions", "Multiplying Numbers Close to 100", "Dividing Fractions", "Multiplying over 37"]
		lmGroupsTwo = ["Squaring Numbers", "Cubing Numbers", "Square Rooting Numbers", "Cube Rooting Numbers", "Adding Square Type One", "Adding Square Type Two", "Difference of squares", "Logarithms"]
		lmGroupsThree = ["Difference of Reverses", "Adding with Common Products", "Adding with Digits and 0's"]
		
		mode, index = pick(options, title, indicator='👉', default_index=1)
		
		player1: Player = Player(username, None, password, newAccount=True)
		
		# 😀 Easy
		if index == 0:
			quizMode = QuizType.EASY
		
		# 😐 Normal
		elif index == 1:
			quizMode = QuizType.NORMAL
		
		# 👺 Hard
		elif index == 2:
			quizMode = QuizType.HARD
		
		elif index == 3:
			quizMode = QuizType.TWO_PLAYER_VS
		
		# ⚙️ Settings
		elif index == 4:
		
			mode2, index2 = pick(settingsOptions, "Settings", indicator='👉', default_index=1)
			if index2 == 0:
				new_password = input("Enter your new password: ")
				player1.changePassword(new_password)
				print(f"{C.BLUE}Password changed, logging out...")
				exit(0)
			if index2 == 1:
				conf, conf2 = pick(["Yes", "No"], "Are you sure?", indicator='👉', default_index=1)
				if conf2 == 0:
					utils.deleteAccount(player1.name)
					exit()
				if conf2 == 1:
					print("Account deletion cancelled.")
					continue
			if index2 == 2:
				utils.giveInfo()
				continue
		
		# 🔒 Administrative Menu
		elif index == 5:
			with open("whitelist.json", "r") as bFile:
				data = json.load(bFile)
			bFile.close()
			for element in data:
				if username == element:
					if input("Enter Password: ") == "admin":
						utils.doThing(player1)
					else:
						print(f"{C.RED}Incorrect password. Aborting...")
						with open("blacklist.json", "w+") as bFile:
							data.append(username)
							json.dump(data, bFile)
						bFile.close()
					exit()
			print("You do not have sufficient permissions to complete this action.  Do not try this again.")
			input("\nPress enter to return to the main menu\n")
			continue
		elif index == 6:
			lmmode, lmgindex = pick(lmGroups, "What topic? ", indicator='👉', default_index=0)
			if lmgindex == 0:
				lmg1mode, lmg1index = pick(lmGroupsOne, "What lesson? ", indicator='👉', default_index=0)
				if lmg1index == 0:
					lm.learn_multiplyBy25()
				if lmg1index == 1:
					lm.learn_multiplyBy75()
				if lmg1index == 2:
					lm.learn_multiplyBy101()
				if lmg1index == 3:
					lm.learn_multiplyBy11()
				if lmg1index == 4:
					lm.learn_multiplyFractions()
				if lmg1index == 5:
					lm.learn_centeredAroundThird()
				if lmg1index == 6:
					lm.learn_remainder()
				if lmg1index == 7:
					lm.learn_compareFractions()
				if lmg1index == 8:
					lm.learn_closeToHundred()
				if lmg1index == 9:
					lm.learn_divideFractions()
				if lmg1index == 10:
					lm.learn_multiplyOver37()
			elif lmgindex == 1:
				lmg2mode, lmg2index = pick(lmGroupsTwo, "What lesson? ", indicator='👉', default_index=0)
				if lmg2index == 0:
					lm.learn_squareNumbers()
				if lmg2index == 1:
					lm.learn_cubeNumbers()
				if lmg2index == 2:
					lm.learn_squareRootNumber()
				if lmg2index == 3:
					lm.learn_cubeRootNumber()
				if lmg2index == 4:
					lm.learn_addSquares3x()
				if lmg2index == 5:
					lm.learn_addSquaresSpec()
				if lmg2index == 6:
					lm.learn_differenceOfSquares()
				if lmg2index == 7:
					lm.learn_logarithms()
			elif lmgindex == 2:
				lmg3mode, lmg3index = pick(lmGroupsThree, "What lesson? ", indicator='👉', default_index=0)
				if lmg3index == 0:
					lm.learn_diffOfReverses()
				if lmg3index == 1:
					lm.learn_addCommon()
				if lmg3index == 2:
					lm.learn_sepDigits()
			else:
				print("Error #1: Not found")
				exit()
			continue
		elif index == 7:
			break
		else:
			print(" Error #2: Not found")
			exit(1)
		
		# ----------------------------------------------------
		player1.current_mode = quizMode
		numQuestions = input("How many questions? >> ")
		while not numQuestions.isnumeric():
			numQuestions = input("Invalid input. How many questions? >> ")
		numQuestions = int(numQuestions)
		
		# If EASY mode
		if quizMode == QuizType.EASY or quizMode == quizMode.NORMAL:
			# player1.current_mode = QuizType.EASY
			input("Press Enter to start\n--------------------")
			start_time = time.time()
			total = main(int(numQuestions), player1)
			end_time = time.time()
			time_lapsed = end_time - start_time
			time_convert(time_lapsed)
			print(f"Score: {player1.calculateScore(total)}")
		
		elif quizMode == QuizType.HARD:
			# player1.current_mode = QuizType.EASY
			print("Error #3: Not implemented")
			print("Hard is not yet implemented. Please try something else.")
			input("Press enter to go back to the main menu")
			continue
		
		elif quizMode == QuizType.TWO_PLAYER_VS:
			# player1.current_mode = QuizType.TWO_PLAYER_VS
			print("Error #3: Not implemented")
			print("2 Player is not implemented. Please try something else.\n")
			input("Press enter to go back to the main menu\n")
			continue
		player1.saveToScoreboard(quizMode)
		
		write_leaderboard(quizMode, player1, total, time_lapsed)
		
		userLeaderboardResponse = input("Display leaderboard? [Y/n] >> ").strip().lower()
		if userLeaderboardResponse == "y" or userLeaderboardResponse == "":
			utils.read_leaderboard(quiztype=quizMode, numQ=int(numQuestions))
			input("\nPress enter to go back to main menu.")
		