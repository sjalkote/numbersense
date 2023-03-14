from pick import pick
import questions
import utils
from tabulate import tabulate
import random


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
    questions.printAnswerValidation(utils.better_num_input("What is 28 divided by 4? "), "7", "7")
    questions.printAnswerValidation(utils.better_num_input("What is 7 times 100? "), "700", "700")
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
    questions.printAnswerValidation(utils.better_num_input("What is 28 divided by 4? "), "7", "7")
    questions.printAnswerValidation(utils.better_num_input("What is 7 times 3? "), "21", "21")
    questions.printAnswerValidation(utils.better_num_input("What is 21 times 100? "), "2100", "2100")
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
    questions.printAnswerValidation(utils.better_num_input("What is the first digit? "), "4", "4")
    questions.printAnswerValidation(utils.better_num_input("What is the second digit? "), "7", "7")
    questions.printAnswerValidation(utils.better_num_input("What is the third digit? "), "3", "3")

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
    questions.printAnswerValidation(utils.better_num_input("15 * 11 = "), "165", "165")
    questions.printAnswerValidation(utils.better_num_input("66 * 11 = "), "726", "726")
    questions.printAnswerValidation(utils.better_num_input("94 * 11 = "), "1034", "1034")


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
    questions.printAnswerValidation(utils.better_frac_input("What is the numerator?"), "8", "8")
    questions.printAnswerValidation(utils.better_frac_input("What is the denominator?"), "3", "3")

    print("""If the opposing numerator and denominators are equal, the answer is the other numerator over the other denominator. For example,
	4/5 * 5/7
	We can cancel out the fives, meaning that the answer is 4/7.
Here are some practice problems:
 """)
    questions.multiplyFractions()
    questions.multiplyFractions()
    questions.printAnswerValidation(utils.better_frac_input("7/5 * 5/6 = "), "7/6", "7/6")


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
    questions.printAnswerValidation(utils.better_num_input("What is the center number? "), "25", "25")
    questions.printAnswerValidation(utils.better_num_input("What is the distance to that number?"), "1", "1")
    questions.printAnswerValidation(utils.better_num_input("What is the difference of 25^2 and 1^2? "), "624", "624")
    print("Here are some example problems.")
    questions.centeredAroundThird()
    questions.centeredAroundThird()
    questions.printAnswerValidation(utils.better_num_input("24 * 28 = "), "672", "672")


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
        questions.printAnswerValidation(utils.better_num_input("What is the remainder of 132 / 3? "), "0", "0")
        questions.printAnswerValidation(utils.better_num_input("What is the remainder of 132 / 9? "), "6", "6")
        questions.printAnswerValidation(utils.better_num_input("What is the remainder of 1532 / 9? "), "2", "2")
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
        questions.printAnswerValidation(utils.better_num_input("What is the remainder of 3804 / 4? "), "0", "0")
        questions.printAnswerValidation(utils.better_num_input("What is the remainder of 91199222 / 4? "), "2", "2")
        questions.printAnswerValidation(utils.better_num_input("What is the remainder of 123123 / 8? "), "3", "3")
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
        questions.printAnswerValidation(utils.better_num_input("After adding the first digit, what do we have? "), "1",
                                        "1")
        questions.printAnswerValidation(utils.better_num_input("After subtracting the second digit, what do we have? "),
                                        "-4", "-4")
        questions.printAnswerValidation(utils.better_num_input("After adding the third digit, what do we have? "), "3",
                                        "3")
        print(
            "The remainder of 157 / 11 is 2. \nRemember, the answer is always the absolute value of the number we end up with. \nHere are some practice problems:")
        questions.printAnswerValidation(utils.better_num_input("What is the remainder of 5143 / 11? "), "5", "5")
        questions.printAnswerValidation(utils.better_num_input("What is the remainder of 1345 / 11? "), "3", "3")
        questions.printAnswerValidation(utils.better_num_input("What is the remainder of 57543 / 11? "), "2", "2")


def learn_compareFractions():
    print("Comparing Fractions")
    print("""
To compare two fractions, we multiply the opposing numerators and denominators, and associate that number with the numerator it corresponds to. Which ever number is larger is the larger of the two fractions.
For example: 2/3 vs 4/5
	Multiplying opposites: 2 * 5 = 10, which is with the first number, and 3 * 4 = 12, which 	is with the second. 
	Because 12 is bigger than 10, 4/5 (Which corresponds with 12) is bigger than 2/3 (Which 	corresponds with 10)
Let's try an example: 3/4 vs 5/6
 """)
    questions.printAnswerValidation(utils.better_num_input("What product corresponds with 3/4? "), "18", "18")
    questions.printAnswerValidation(utils.better_num_input("What product corresponds with 5/6? "), "20", "20")
    questions.printAnswerValidation(utils.better_frac_input("20 is greater than 18. So which fraction is bigger? "),
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
    questions.printAnswerValidation(questions.better_num_input("What are the first three digits? (Sum + 100) "), "109",
                                    "109")
    questions.printAnswerValidation(questions.better_num_input("What are the last two digits? (Product) "), "20", "20")
    print("Yes. 104 * 105 is 10920")
    print("""Multiplying two numbers below one hundred is more or less similar. You add up the distances from 100 and subtract that from 100 for the first two digits, and multiply the distances from 100 for the last two digits. For example:
 	98 * 96
  	The sum of the distances from 100 (2 and 4, respectively) is 6. 100 - 6 = 94
   	The product of these distances is 8, which we add a zero to as it is only one digit.
	So, 
 	98 * 96 = 9408
  	Let's try one together: 97 * 95
 	""")
    questions.printAnswerValidation(questions.better_num_input("What is the sum of the distances from 100? "), "8", "8")
    questions.printAnswerValidation(questions.better_num_input("What is 100 - 8? "), "92", "92")
    questions.printAnswerValidation(questions.better_num_input("What is the product of the distances from 100? "), "15",
                                    "15")
    questions.printAnswerValidation(questions.better_num_input("What is the answer? "), "9215", "9215")
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
    questions.printAnswerValidation(utils.better_frac_input("What is the numerator? "), "8", "8")
    questions.printAnswerValidation(utils.better_frac_input("What is the denominator? "), "9", "9")
    print("Yes. The answer would be 8/9")
    print("""If both the numerators are equal, the answer is the second denominator over the first denominator. If the denominators are equal, the answer is the first numerator over the second.
Example #1: 
	3/2 ➗ 3/4 = 4/2 = 2
Example #2:
	2/3 ➗ 4/3 = 2/4 = 1/2
 """)
    questions.divideFractions()
    questions.printAnswerValidation(utils.better_frac_input("5/7 ➗ 5/6 = "), "6/7", "6/7")
    questions.printAnswerValidation(utils.better_frac_input("3/4 ➗ 5/4 = "), "3/5", "3/5")


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
	Squaring numbers from 41-60 is very easy. First, we subtract 50 from that number, and then add that difference to 25. Then, we square the difference and put that at the end. For example, 
	48 ^ 2
	48 - 50 = -2
	25 + (-2) = 23
	(-2) ^ 2 = 4
	48 ^2 = 2304
	Let's try one together: 53^2
	""")
    questions.printAnswerValidation(utils.better_num_input("What is the difference? "), "3", "3")
    questions.printAnswerValidation(utils.better_num_input("What are the first two digits? (25 + that number) "), "28",
                                    "28")
    questions.printAnswerValidation(utils.better_num_input("What is the last digit? (Difference squared)? "), "9", "9")
    print("Yes. The answer is 2809")
    print("Squaring numbers ending in 5.")
    print("""
	To square a number ending in 5, you take the first digit, multiply it by itself + 1, then append 25. For example, 
 	25 ^ 2
  	The first digit (2) times itself plus one (3) is 6.
   	We append 25 to get 625.
 """)
    input("Press enter to continue")
    print("Squaring other numbers.")
    print("You can square any other number with this trick:")
    print("""
To square a number, you add the ones digit, then multiply by the tens digit, then finally append the ones digit squared at the end. For example:
    22^2
    22 + 2(The ones digit) = 24
    24 * 2(The tens digit) = 48
    The ones digit (2) squared is 4
    And we append that the end to get 484.
    22 ^ 2 = 484
    Remember to carry over if the ones digit squared is more than one digit.
    Let's try one together: 24 ^ 2
    """)
    questions.printAnswerValidation(utils.better_num_input("After adding the ones digit, what do we have? "), "28",
                                    "28")
    questions.printAnswerValidation(utils.better_num_input("After multiplying by the tens digit, what do we have? "),
                                    "56", "56")
    questions.printAnswerValidation(utils.better_num_input("After appending the ones digit squared, what do we have? "),
                                    "576", "576")
    print("Yes. Now, let's try some practice problems over these tricks.")
    questions.printAnswerValidation(utils.better_num_input("What is 43 ^ 2? "), "1849", "1849")
    questions.printAnswerValidation(utils.better_num_input("What is 56 ^ 2? "), "3136", "3136")
    questions.printAnswerValidation(utils.better_num_input("What is 65 ^ 2? "), "4225", "4225")
    questions.printAnswerValidation(utils.better_num_input("What is 27 ^ 2? "), "729", "729")
    questions.printAnswerValidation(utils.better_num_input("What is 31 ^ 2? "), "961", "961")


def learn_cubeNumbers():
    print("""There are no viable tricks to cube numbers. Because the numbers you will have to cube will mostly be below 15 anyway, however, it is best to memorize your cubes up to 15. Here:
    1^3 = 1
    2^3 = 8
    3^3 = 27 
    4^3 = 64
    5^3 = 125
    """)
    input("Press enter to continue")
    print("""
        6^3 = 216
        7^3 = 343
        8^3 = 512
        9^3 = 729
        10^3 = 1000
        11^3 = 1331
        12^3 = 1728
        13^3 = 2197
        14^3 = 2744
        15^3 = 3375
    
        Here are a few practice problems:
    """)
    questions.cubeNumber()
    questions.cubeNumber()
    questions.cubeNumber()


def learn_squareRootNumber():
    list = ["0", "1 or 9", "No rational square root", "No rational square root", "2 or 8", "5", "4 or 6",
            "No rational square root", "No rational square root", "3 or 7", ]
    print("Square rooting numbers")
    print("Taking the square root of numbers quickly requires a good amount of memorization. First, we use the last "
          "digit of the square and see what last digits of the roots they correspond to. Here is the table:")

    print(tabulate({"Last digit of Square": [num for num in range(10)], "Last digit of Square root": list},
                   headers="keys"))
    print("""Finally, we find what multiply-of-ten squares the square is between and which one it is closer to in order to figure out the first digit and the second digit in the case of multiply options. For example:
    Square root of 2704
    Because 4 means 2 or 8 as the last digit (Based on the table), we 	know the last digit of the root is 2 or 8. 
    Because 2704 is between 2500 (50^2) and 3600 (60^2), we know the first digit is 5.
    And finally, since 2704 is closer to 2500 (50^2), we know it ends in two rather than 8.
    Let's try one together: Square root of 1681
    1 corresponds with 1 or 9 according to the table.
    """)
    questions.printAnswerValidation(
        utils.better_num_input("What is the tens digit? (Find what multiple-of-ten squares it is between) "), "4", "4")
    questions.printAnswerValidation(
        utils.better_num_input("What is the ones digit? (1 or 9, is it closer to 40^2 or 50^2?) "), "1", "1")
    print("Yes. The answer is 41 \nHere are some practice problems.")
    questions.squareRootNumber()
    questions.squareRootNumber()
    questions.squareRootNumber()


def learn_cubeRootNumber():
    last_digit_of_cube_root = [0, 1, 8, 7, 4, 5, 6, 3, 2, 9]
    print("Cube rooting numbers")
    print(
        "Finding the cube root of numbers is very similar to finding the square root of numbers. The main differences "
        "are that the table is slightly different and that there are no ors. We also have to use multiple-of-ten cubes "
        "rather than squares. Here is the table:"
    )
    print(
        tabulate({"Last digit of cube": [num for num in range(10)], "Last digit of cube root": last_digit_of_cube_root},
                 headers="keys"))
    print("""For example,
    The cube root of 148877
    First, we see that the ending of the cube (7) corresponds with the ending of the cube root (3). Next, we see that 148,877 is between 50^3 (125000) and 60^3 (216000).
    This means the first digit is 5 and the last digit is 3, to get a cube root of 53.
    Let's try one together: the cube root of 74,088
    """)
    questions.printAnswerValidation(
        utils.better_num_input("According to the table, what would the cube root end with? "),
        "2", "2")
    questions.printAnswerValidation(
        utils.better_num_input("Based on what cubes it is between, what is the first digit? "), "4", "4")
    print("Yes. The answer is 42. \nLet's try some practice problems.")
    questions.cubeRootNumber()
    questions.cubeRootNumber()
    questions.cubeRootNumber()


def learn_addSquares3x():
    print("Adding squares with x and 3x")
    print("""
    This is a specific type of adding squares. When adding the square of a number and the square of three times that number, the answer is simply the number squared times 10. For example,
    20^2 + 60^2
    Because 60 is three times 20, this rule applies.
    20^2 is 400, times 10 is 4000, which is our answer.
    Let's try some practice problems:
    """)
    questions.addSquares(1)
    questions.addSquares(1)
    questions.addSquares(1)


def learn_addSquaresSpec():
    print("Adding squares with special case")
    print("""
    In specific scenarios, adding squares can be very easy. 
    Let's take numbers ab and cd
    Adding ab^2 and cd^2 where c = b - 1 and a + d = 10, the answer is (a^2 + b^2) * 101.
    For example,
    32^2 + 17^2
    Because 1 is one less than 2 and 3 + 7 = 10, the rule applies
    The answer is simply (3^2 + 2^2) * 101
    (9 + 4) * 101
    13 * 101
    32^2 + 17^2 = 1313
    Remember to arrange the numbers so that they are in the correct order.
    Here are some practice problems:
 """)
    questions.addSquares(2)
    questions.addSquares(2)
    questions.addSquares(2)


def learn_differenceOfSquares():
    print("Difference of squares")
    print("""
    Differences of squares are very easy. 
    a^2 - b^2 is (a + b)(a - b)
    For example,
    10^2 - 8^2 = (10 + 8) * (10 - 8)
    18 * 2 = 36
    10^2 - 8^2 = 36
    Here are some practice problems:
    """)
    questions.differenceOfSquares()
    questions.differenceOfSquares()
    questions.differenceOfSquares()


def learn_logarithms():
    print("Logarithms")
    print("""
    The major part of doing logarithms in your head is ensuring that you know how to rethink them. log base a (c) = b means b^a = c
    For example,
    log base 3 of 81 means 3 to the power of what is 81.
    Because 3^4 is 81, the answer is 4.
    Here are some practice problems:
    """)
    questions.logarithmQuestion()
    questions.logarithmQuestion()
    questions.logarithmQuestion()


def learn_diffOfReverses():
    print("Difference of reverses.")
    print("""
    Subtracting reverses is very easy. It works with three digit numbers and four digit numbers with zeros in the middle. You find the difference of the first digits, multiply it by 100 or 1000 depending on the number of digits, then subtract the difference again. For example,
    321 - 123
    3-1 = 2
    2 * 100 - 2 = 198
    321 - 123 = 198
Example #2:
    2004 - 4002
    2 - 4 = -2
    -2 * 1000 - (-2) = -1998
    2004 - 4002 = -1998
    Let's try some practice problems.
    """)
    questions.differenceOfReverses(random.randint(3, 4))
    questions.differenceOfReverses(random.randint(3, 4))
    questions.differenceOfReverses(random.randint(3, 4))


def learn_addCommon():
    print("Adding common factors")
    print("""
    To add two numbers multiplied by the same number, the answer is the the sum of the two numbers multiplied by the other. For example,
    17 * 10 + 13 * 10
    This is the same as (17 + 13) * 10, or 30 * 10 = 300.
    Here are some practice problems:
    """)
    questions.addCommonProducts()
    questions.addCommonProducts()
    questions.addCommonProducts()


def learn_sepDigits():
    print("Adding with numbers and 0's")
    print("""
    This can be done very easily. A lot of questions like this will split up 5 digits between two numbers and have one 0 and one number for each place value. For example:
    103.4 + 12.05
    Hundreds: 1
    Tens: 2
    Ones: 3
    Tenths: 4
    Hundreths: 5
    The answer is 123.45
    Here are some practice problems:
    """)
    questions.sepDigits()
    questions.sepDigits()
    questions.sepDigits()


# Data & Algebra

def learn_gcflcm():
    print("Finding the GCF, LCM, and the product of the two.")
    print("""
    Finding gcf is very simple and doesn't usually require a trick. For example:
    16 and 20
    The greatest common factor of these two is easily 4, as it is the largest number that goes into both. 
    """)
    input("Press enter to continue. ")
    print("""LCM can have a trick, however. Remember that the LCM of two numbers is equal to their product over their GCF. For example:
    16 and 20
    GCF = 4
    16 * 20 = 320
    320/4 = 80
    The least common multiple is 80.
 """)
    input("Press enter to continue. ")
    print("""Finally, remember that lcm(x,y) * gcf(x,y) = x * y. For example,
    GCF(14,18) * LCM(14,18) = 14 * 18
    14 * 18 = 252
    Here are some practice problems:
    """)
    questions.gcflcmQuestion()
    questions.gcflcmQuestion()
    questions.gcflcmQuestion()


def learn_stats():
    print("Statistics")
    print("""
Most statistic questions are really quite easy.
Range: Biggest number minus smallest number
Median: Middle number 
Mean: Sum of the numbers over the number of numbers

Let's take the set of numbers: 1,2,3,4,5
5 (Biggest) - 1 (Smallest) = 4, or the range
Because there are 5 numbers, the middle number is the third one ((num + 1)/2). The third number, or 3, is the median.
The sum of all the numbers is 1 + 2 + 3 + 4 + 5, or 15.
15 / 5(Number of numbers) is 3, or our mean.

Example #2:
26, 30, 6, 17, 11
30 - 6 = 24, or the range
3rd is median. 6, 11, 17 (Smallest to biggest)
26 + 30 + 6 + 17 + 11 = 90
90 / 5 = 18
Mean: 18 
    Let's try out the set: 23,18,10,9,16
    """)
    questions.printAnswerValidation(utils.better_num_input("What is the range? "), "14", "14")
    questions.printAnswerValidation(utils.better_num_input("What is the median? "), "16", "16")
    questions.printAnswerValidation(utils.better_frac_input("What is the mean? "), "15.2", "15.2")


def learn_integralDivisors():
    print("Finding the number of integral divisors.")
    print("""
    To find the number of integral divisors, we have to create a prime factorization and multiply all of the exponents plus one. For example,
    How many integral divisors does 24 have?
    The prime factorization of 24 is 2^3 * 3^1
    (3 + 1) * (1 + 1) = 4 * 2 = 8
    24 has 8 integral divisors.

    In order to apply this trick efficiently, practice is key.
    Here are some practice problems:
    """)
    questions.integralDivisorsQuestion()
    questions.integralDivisorsQuestion()
    questions.integralDivisorsQuestion()


def learn_subsets():
    print("Find the Number Of Subsets")
    print("""
    Finding the number of subsets is very simple. The number of subsets is equal to two to the power of the number of elements in the set, and the number of proper subsets is one less than that. For example,
    A 3 element set has how many subsets?
    2^3 = 8
    It would have 8 subsets.
    Example #2:
    A 3 element set has how many PROPER subsets?
    2^3 = 8
    8 - 7
    It has 7 proper subsets.

    Here are some practice problems
 """)
    questions.subsetsQuestion()
    questions.subsetsQuestion()
    questions.subsetsQuestion()


def learn_OrderofOperations():
    print("Order of operations.")
    print("""
    In order to do order of operations, all you have to do is keep in mind PEMDAS:
    Parentheses
    Exponents
    Multiplication and
    Divison
    Addition and
    Subtraction

    Evaluate in this order, and you will be able to do the questions fine.
    """)
    questions.orderOfOperationsQuestion()
    questions.orderOfOperationsQuestion()
    questions.orderOfOperationsQuestion()


def learn_xtoy1():
    print("Algebra with changing the exponent.")
    print("""
    These problems generally involve identifying what needs to be done and keeping in mind that adding one to the exponent is the same as multiplying by the base number. For example, 
    Let's say 3^(x-1) = 4
    This means that 3^x = 4 * 3, or 12
    If 3^(x+1) = 24, then we subtract one from the exponent, or divide by the base number. 24 / 3 = 8.
    Finally, let's say 3^.5x = 4. When we multiply the exponent by 2, we simply square. So in this case, 3^x = 4^2, or 16.
    Keep these tricks in mind when trying the following problem practice:
    """)
    questions.xtoy1()
    questions.xtoy1()
    questions.xtoy1()


def learn_xAndYCubed():
    print("Algebra with X and Y cubed")
    print("""
    Even knowing the trick, this is one of the harder types of questions.
    Let's take these equations:
    x + y = 3
    xy = 2
    What is x + y?
    Simplifying the equations, we can see that
    x + y is equal to (x + y)^3 - 3xy(x + y)
    So in this equation, the answer is 3^3 - 3 * 2 * 3, or 9
    This trick requires a lot of practice to perfect. 
    Here are some practice problems:
    """)
    questions.xAndyCubed()
    questions.xAndyCubed()
    questions.xAndyCubed()
