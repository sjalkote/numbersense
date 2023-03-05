from pick import pick
import questions
import utils


# epic progress on learn mode :D

# Multiplication, Division, and Fractions

# Multiplication
def learn_multiplyBy25():
    print("Multiplying by 25")
    print("""
Multiplying by 25 is quite simple. To multiply a number by 25, you can simply divide that number by four then multiply that by 100. For example,
	36 * 25
	36 / 4 = 9
	9 * 100 = 900
	36 * 25 = 900
	Let's try 28 * 25.
""")
    questions.printAnswerValidation(utils.betterNumInput("What is 28 divided by 4? "), "7", "7")
    questions.printAnswerValidation(utils.betterNumInput("What is 7 times 100? "), "700", "700")
    print("There. 28 * 25 = 700.")
    print("""For dividing numbers that aren't divisible by four,
the trick still applies. When there is a remainder of 1, add a 25, when there is a remainder of 2, add a 50, 3 a 75.
	  Here is an example with a remainder of 3:
	19 * 25 
	The largest multiple of four less than 19 is 16.
   	16 / 4 = 4
	4 * 100 = 400
	The remainder is 3, so we add a 75.
	19 * 25 = 475
 	Here are some practice problems:
 """)
    questions.multiplyBy(randFactor=25)
    questions.multiplyBy(randFactor=25, diffTypes=True)
    questions.multiplyBy(randFactor=25, diffTypes=True)


def learn_multiplyBy75():
    print("Multiplying by 75")
    print("""
Multiplying by 75 is quite simple. To multiply a number by 75, you can simply divide that number by four then multiply that by 3 and then 100. For example,
	  36 * 75
   	  36 / 4 = 9
	  9 * 3 = 27 
	  27 * 100 = 2700
      36 * 25 = 2700
	Let's try 28 * 75.
""")
    questions.printAnswerValidation(utils.betterNumInput("What is 28 divided by 4? "), "7", "7")
    questions.printAnswerValidation(utils.betterNumInput("What is 7 times 3? "), "21", "21")
    questions.printAnswerValidation(utils.betterNumInput("What is 21 times 100? "), "2100", "2100")
    print("There. 28 * 75 = 2100.")
    print("""
For dividing numbers that aren't divisible by four,
the trick still applies. When there is a remainder of 1, add a 75, when there is a remainder of 2, add a 150, 3 a 225.
	  Here is an example with a remainder of 3:
	19 * 75
	The largest multiple of four less than 19 is 16.
   	16 / 4 = 4
	4 * 3
	12 * 100 = 1200
	The remainder is 3, so we add a 225.
	19 * 75 = 1425
 	Here are some practice problems:
 """)
    questions.multiplyBy(randFactor=75)
    questions.multiplyBy(randFactor=75, diffTypes=True)
    questions.multiplyBy(randFactor=75, diffTypes=True)


def learn_multiplyBy101():
    print("Multiplying by 101")
    print("""
 Multiplying by 101 with two digit numbers is very simple. You simply repeat the number. For example,
	21 * 101 = 2121
Here are some practice problems:
 """)
    questions.multiplyBy(randFactor=101)
    questions.multiplyBy(randFactor=101)
    questions.multiplyBy(randFactor=101)


def learn_multiplyBy11():
    print("Multiplying by 11.")
    print("""
Multiplying two digit numbers by 11 is a very easy trick. The first digit of the answer is the first number. The second digit is the sum of the digits, and the third digit of the answer is the second digit of the number. For example:
	18 * 11
 	First digit: 1
  	Second digit: 1 + 8 = 9
    Third digit: 8
	18 * 11 = 198
 	Let's try an example: 43 * 11""")
    questions.printAnswerValidation(utils.betterNumInput("What is the first digit? "), "4", "4")
    questions.printAnswerValidation(utils.betterNumInput("What is the second digit? "), "7", "7")
    questions.printAnswerValidation(utils.betterNumInput("What is the third digit? "), "3", "3")

    print("""Correct, 43 * 11 = 473
 Occasionally, the sum of the two digits will be more than 10. In that case, we carry the first digit of the sum to the first digit of the answer. For example,
	28 * 11
 	First digit: 2
  	Second digit: 2+8 = 10. Because this is two digits, we carry over the 1. This makes the first digit 3.
	Third digit: 8
	28 * 11 = 308
	If the sum of the digits makes the first digit more than 10, the answer will have 4 digits.
 	(98 * 11 = 1078)
  	Here are some example problems:
 """)
    questions.printAnswerValidation(utils.betterNumInput("15 * 11 = "), "165", "165")
    questions.printAnswerValidation(utils.betterNumInput("66 * 11 = "), "726", "726")
    questions.printAnswerValidation(utils.betterNumInput("94 * 11 = "), "1034", "1034")


def learn_multiplyFractions():
    print("Multiply fractions")
    print("""
To multiply fractions, you multiply the numerators(Top numbers) and the denominators(Bottom numbers), then simplify.
For example,
	3/4 * 2/5
	3 * 2 / 4 * 5
	6/20 = 3/10
	3/4 * 2/5 = 3/10
Here's a simple example: 
	2/1 * 4/3 = """)
    questions.printAnswerValidation(utils.betterFracInput("What is the numerator?"), "8", "8")
    questions.printAnswerValidation(utils.betterFracInput("What is the denominator?"), "3", "3")

    print("""If the opposing numerator and denominators are equal, the answer is the other numerator over the other denominator. For example,
	4/5 * 5/7
	We can cancel out the fives, meaning that the answer is 4/7.
Here are some practice problems:
 """)
    questions.multiplyFractions()
    questions.multiplyFractions()
    questions.printAnswerValidation(utils.betterFracInput("7/5 * 5/6 = "), "7/6", "7/6")


def learn_centeredAroundThird():
    print("Multiply two numbers centered around a third number")
    print("""
If two numbers are centered around another, their product can be found quite easily. The product is equal to the center number squared minus the distance to that number squared. For example:
13 * 17
Center number: 15
Distance to that number: 2
15 ^ 2 - 2 ^ 2 = 225 - 4 = 221
13 * 17 = 221
Let's try an example: 24 * 26
 """)
    questions.printAnswerValidation(utils.betterNumInput("What is the center number? "), "25", "25")
    questions.printAnswerValidation(utils.betterNumInput("What is the distance to that number?"), "1", "1")
    questions.printAnswerValidation(utils.betterNumInput("What is the difference of 25^2 and 1^2? "), "624", "624")
    print("Here are some example problems.")
    questions.centeredAroundThird()
    questions.centeredAroundThird()
    questions.printAnswerValidation(utils.betterNumInput("24 * 28 = "), "672", "672")


def learn_remainder():
    optNums = ["3 and 9", "4 and 8", "11"]
    remainderNum, index = pick(optNums, "What remainder?", indicator="👉")
    if index == 0:
        print("""To divide by 3 and 9, we add up the digits, then check if the sum of the digits is divisble by 3 or 9. For example,
  to check if 147 is divisible by three, we can add up 1, 4, and 7. The sum of these three numbers is 12. We can easily see that this is divisible by three, but we can also add the digits of 12 to double check: 1 + 2 = 3, which is divisible by three. 
Example #2: 
	Remainder of 78 / 9:
 	7 + 8 = 15
  	1 + 5 = 6
   	The remainder of 78 / 9 is 6.
   	Here are some practice problems:
  """)
        questions.printAnswerValidation(utils.betterNumInput("What is the remainder of 132 / 3? "), "0", "0")
        questions.printAnswerValidation(utils.betterNumInput("What is the remainder of 132 / 9? "), "6", "6")
        questions.printAnswerValidation(utils.betterNumInput("What is the remainder of 1532 / 9? "), "2", "2")
    elif index == 1:
        print("""
To divide by 4 or 8, we simply look at the last digits, and if they are divisible by 4 or 8, their remainder is the remainder for the whole number. For dividing by 4, we look at the last two digits, for dividing by 8, the last three.
For example:
	2144 / 4
	We only look at 44 (The last two digits)
	Since 44 is divisible by 4, the entire number is as well.
Example #2:
	39300 / 8
 	We only look at 300 (The last three digits)
  	Because 300 / 8 has a remainder of 4, the remainder of 39300/ 8 is 4.
   	Here are some practice problems:
  """)
        questions.printAnswerValidation(utils.betterNumInput("What is the remainder of 3804 / 4? "), "0", "0")
        questions.printAnswerValidation(utils.betterNumInput("What is the remainder of 91199222 / 4? "), "2", "2")
        questions.printAnswerValidation(utils.betterNumInput("What is the remainder of 123123 / 8? "), "3", "3")
    elif index == 2:
        print("""
To check divisibility by 11, we add and subtract alternate digits.
Example:
	435 / 11
 	We add 4, to get 4.
  	We subtract 3, to get 1.
	We then add 5, to get 6.
 	The remainder of 435 / 11 is 6.
  	Let's try one together: 157
  """)
        questions.printAnswerValidation(utils.betterNumInput("After adding the first digit, what do we have? "), "1",
                                        "1")
        questions.printAnswerValidation(utils.betterNumInput("After subtracting the second digit, what do we have? "),
                                        "-4", "-4")
        questions.printAnswerValidation(utils.betterNumInput("After adding the third digit, what do we have? "), "3",
                                        "3")
        print(
            "The remainder of 157 / 11 is 2. \nRemember, the answer is always the absolute value of the number we end up with. \nHere are some practice problems:")
        questions.printAnswerValidation(utils.betterNumInput("What is the remainder of 5143 / 11? "), "5", "5")
        questions.printAnswerValidation(utils.betterNumInput("What is the remainder of 1345 / 11? "), "3", "3")
        questions.printAnswerValidation(utils.betterNumInput("What is the remainder of 57543 / 11? "), "2", "2")


def learn_compareFractions():
    print("Comparing Fractions")
    print("""
To compare two fractions, we multiply the opposing numerators and denominators, and associate that number with the numerator it corresponds to. Which ever number is larger is the larger of the two fractions.
For example: 2/3 vs 4/5
	Multiplying opposites: 2 * 5 = 10, which is with the first number, and 3 * 4 = 12, which 	is with the second. 
	Because 12 is bigger than 10, 4/5 (Which corresponds with 12) is bigger than 2/3 (Which 	corresponds with 10)
Let's try an example: 3/4 vs 5/6
 """)
    questions.printAnswerValidation(utils.betterNumInput("What product corresponds with 3/4? "), "18", "18")
    questions.printAnswerValidation(utils.betterNumInput("What product corresponds with 5/6? "), "20", "20")
    questions.printAnswerValidation(utils.betterFracInput("20 is greater than 18. So which fraction is bigger? "),
                                    "5/6", "5/6")
    print("5/6 is greater. \nHere are some practice problems.")
    questions.compareFractions()
    questions.compareFractions()
    questions.compareFractions()


def learn_closeToHundred():
    print("Multiplying two numbers close to one hundred.")
    print("""
To multiply two numbers close to a hundred that are more than one hundred, we look at their tens and ones digits. We multiply these digits and add these digits to get our product. For example:
	102 * 103
	First, we take the tens & ones digits, 2 and 3. Added together, these are 5, and added to 	a hundred, they are 105. These are the first three digits of our answer. 
	Next, we multiply 3 and 2 to get 6. We append this at the end, along with a zero if it is 	only one digit. We append 06 to get 10506.
	102 * 103 = 10506
Let's try an example together: 105 * 104
 """)
    questions.printAnswerValidation(questions.betterNumInput("What are the first three digits? (Sum + 100) "), "109",
                                    "109")
    questions.printAnswerValidation(questions.betterNumInput("What are the last two digits? (Product) "), "20", "20")
    print("Yes. 104 * 105 is 10920")
    print("""Multiplying two numbers below one hundred is more or less similar. You add up the distances from 100 and subtract that from 100 for the first two digits, and multiply the distances from 100 for the last two digits. For example:
 	98 * 96
  	The sum of the distances from 100 (2 and 4, respectively) is 6. 100 - 6 = 94
   	The product of these distances is 8, which we add a zero to as it is only one digit.
	So, 
 	98 * 96 = 9408
  	Let's try one together: 97 * 95
 	""")
    questions.printAnswerValidation(questions.betterNumInput("What is the sum of the distances from 100? "), "8", "8")
    questions.printAnswerValidation(questions.betterNumInput("What is 100 - 8? "), "92", "92")
    questions.printAnswerValidation(questions.betterNumInput("What is the product of the distances from 100? "), "15",
                                    "15")
    questions.printAnswerValidation(questions.betterNumInput("What is the answer? "), "9215", "9215")
    print(
        "\nSometimes, the product will be three digits. In this case, we carry over the first digit into the 100's place and combine it with the last number of the sum.\nLet's try some practice problems.")
    questions.closeToHundred()
    questions.closeToHundred()
    questions.closeToHundred()


def learn_divideFractions():
    print("Divide fractions")
    print("""
To divide fractions, the answer is numerator one x denominator two over numerator two x denominator one
For example,
	3/4 ➗ 2/5
  	3 * 5 ➗ 2 * 4
   	15/8
Here's a simple example: 
	2/3 ➗ 3/4 = """)
    questions.printAnswerValidation(utils.betterFracInput("What is the numerator? "), "8", "8")
    questions.printAnswerValidation(utils.betterFracInput("What is the denominator? "), "9", "9")
    print("Yes. The answer would be 8/9")
    print("""If both the numerators are equal, the answer is the second denominator over the first denominator. If the denominators are equal, the answer is the first numerator over the second.
Example #1: 
	3/2 ➗ 3/4 = 4/2 = 2
Example #2:
	2/3 ➗ 4/3 = 2/4 = 1/2
 """)
    questions.divideFractions()
    questions.printAnswerValidation(utils.betterFracInput("5/7 ➗ 5/6 = "), "6/7", "6/7")
    questions.printAnswerValidation(utils.betterFracInput("3/4 ➗ 5/4 = "), "3/5", "3/5")


def learn_multiplyOver37():
    print("Multiplying over 37")
    print("""
Because 37 is a factor of 111, we can do fun stuff with it. For example, 222/37 is a whole number (6). We can multiply repeating numbers by a two digit number over 37 and end up with a whole number. To do this, we multiply the number over 37 by the repeating number and then by 3. For example,

444 * 2/37
The repeating number 4, multiplied by 2, then multiplied by 3 is our answer. 4 * 2 * 3 = 24, so
444 * 2/37 = 24.

Example #2:
222 * 7/37 = 2 * 7 * 3 = 42

Let's try some practice problems.
 """)
    questions.multiplyOver37()
    questions.multiplyOver37()
    questions.multiplyOver37()


def learn_squareNumbers():
    print("Squaring Numbers")
    print("Squaring Numbers from 41-60")
    print("""
Squaring numbers from 41-60 is very easy. Firs 
 """)
