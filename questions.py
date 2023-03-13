import random
from colorama import init as colorama_init, Fore as C, Style

colorama_init(True)
import math as m
from utils import better_num_input, better_frac_input

RESET = Style.RESET_ALL

multiplyFactors = [25, 25, 25, 75, 75, 101, 11, 11, 11, 111, 101]
remainderFactors = [3, 3, 3, 3, 4, 4, 8, 9, 9, 9, 11, 11, 11]
logFactors = [2, 4, 5, 10]
operations = ["*", "+", "-"]
normBaseFractions = [2,4,5,8,10,20,40]

def printAnswerValidation(uinput, ans, returnAns, twoPlayer=False):
    """Returns whether the question was answered correctly"""
    # TODO: Have an option for multiple attempts, skips the question if pressing enter with empty answer
    if twoPlayer:
        pass
    else:
        if uinput == ans:
            print(f"{C.GREEN}✅ Correct")
            return True
        else:
            print(f"{C.RED}❌ Incorrect.{RESET} Answer is {returnAns}")
            return False


def multiplyBy(randFactor=None, diffTypes=False):
    if randFactor == None:
        factor = random.choice(multiplyFactors)
    else:
        factor = randFactor
    if diffTypes:
        multiple = random.randint(11, 30)
    else:
        multiple = random.randint(3, 25) * 4
    answer = better_num_input(f"{multiple} x {factor} = ")
    return printAnswerValidation(answer, str(int(multiple * factor)), str(int(multiple * factor)))


def divideBy(factor):
    """divides a thing"""
    multiplier = random.randint(1, 20)
    product = multiplier * factor
    # answer = input(f"{product} ➗ {factor} = ")
    answer = better_num_input(f"{product} ➗ {factor} = ")
    return printAnswerValidation(answer, str(int(product / factor)), str(int(product / factor)))


def multiplyFractions():
    num1 = 1
    num2 = 1
    den1 = 1
    den2 = 1
    while den1 == 1 or den2 == 1:
        num1 = random.randint(1, 9)
        num2 = random.randint(1, 9)
        den1 = random.randint(2, 9)
        den2 = random.randint(2, 9)
        gcfOne = getgcf(num1, den1)
        gcfTwo = getgcf(num2, den2)
        num1 /= gcfOne
        num2 /= gcfTwo
        den1 /= gcfOne
        den2 /= gcfTwo
    numFinal = num1 * num2
    denFinal = den1 * den2
    gcfFinal = getgcf(numFinal, denFinal)
    numFinal /= gcfFinal
    denFinal /= gcfFinal
    product = numFinal / denFinal
    uinput = better_frac_input(f"{int(num1)}/{int(den1)} x {int(num2)}/{int(den2)} = ")
    if denFinal == 1:
        return printAnswerValidation(eval(uinput), product, int(numFinal))
    return printAnswerValidation(eval(uinput), product, f"{int(numFinal)}/{int(denFinal)}")


def getgcf(a, b):
    if b == 0:
        return abs(a)
    else:
        return getgcf(b, a % b)


def getlcm(a, b):
    return a * b / getgcf(a, b)


def integralDivisors(a):
    num = 0
    for i in range(1, a + 1):
        if a % i == 0:
            num += 1
    return num


def centeredAroundThird():
    factor = random.randint(1, 4)
    num = random.randint(0, 9) * 10 + 5
    uinput = better_num_input(f"{num - factor} x {num + factor} = ")
    answer = (num - factor) * (num + factor)
    return printAnswerValidation(eval(uinput), answer, answer)


def squareNumber(easy=False):
    if easy:
        numt = random.randint(1, 2)
        match numt:
            case 1:
                num = random.randint(11, 30)
            case 2:
                num = random.randint(41, 60)
    else:
        num = random.randint(11, 60)
    answer = num * num
    uinput = better_num_input(f"What is {num} squared? ")
    return printAnswerValidation(int(uinput), answer, answer)


def cubeNumber():
    num = random.randint(2, 15)
    answer = num * num * num
    uinput = better_num_input(f"What is {num} cubed? ")
    return printAnswerValidation(int(uinput), answer, answer)


def squareRootNumber():
    num = random.randint(11, 100)
    answer = num
    uinput = better_num_input(f"What is the square root of {num * num}? ")
    return printAnswerValidation(int(uinput), answer, answer)


def cubeRootNumber():
    num = random.randint(11, 100)
    answer = num
    uinput = better_num_input(f"What is the cube root of {num * num * num}? ")

    return printAnswerValidation(int(uinput), answer, answer)


def differenceOfReverses(digits):
    if digits == 3:
        num1 = random.randint(1, 9)
        num2 = random.randint(1, 9)
        num3 = random.randint(1, 9)
        answer = (100 * num1 + 10 * num2 + num3) - (100 * num3 + 10 * num2 + num1)
        uinput = better_frac_input(f"{num1}{num2}{num3} - {num3}{num2}{num1} = ")
        return printAnswerValidation(int(uinput), answer, answer)

    if digits == 4:
        num1 = random.randint(1, 9)
        num2 = random.randint(1, 9)
        answer = (1000 * num1 + num2) - (1000 * num2 + num1)
        uinput = int(better_num_input(f"{num1}00{num2} - {num2}00{num1} = "))
        return printAnswerValidation(int(uinput), answer, answer)


def lcmQuestion():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    answer = getlcm(num1, num2)
    uinput = better_num_input(f"lcm({num1},{num2}) = ")

    return uinput, answer


def gcfQuestion():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)

    answer = getgcf(num1, num2)
    uinput = better_num_input(f"gcf({num1},{num2}) = ")

    return uinput, answer


def gcfxlcmQuestion():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    answer = num1 * num2
    uinput = better_num_input(f"gcf({num1},{num2}) x lcm({num1},{num2}) = ")

    return uinput, answer


def addSquares(type):
    if type == 1:
        num1 = random.randint(1, 20)
        uinput = better_num_input(f"{num1} squared + {num1 * 3} squared? ")
        answer = num1 * num1 * 10

    if type == 2:
        dig11 = random.randint(1, 9)
        dig12 = random.randint(1, 9)
        dig21 = dig12 - 1
        dig22 = 10 - dig11
        num1 = 10 * dig11 + dig12
        num2 = 10 * dig21 + dig22
        uinput = better_num_input(f"{num1} squared + {num2} squared? ")
        answer = num1 * num1 + num2 * num2
    return printAnswerValidation(int(uinput), answer, answer)


def remainder():
    num1 = random.randint(1, 100000)
    num2 = random.choice(remainderFactors)
    answer = num1 % num2
    uinput = better_num_input(f"Remainder of {num1} / {num2} = ")

    return printAnswerValidation(int(uinput), answer, answer)


def gcflcmQuestion():
    type = random.randint(1, 3)
    match type:
        case 1:
            uinput, answer = gcfQuestion()
        case 2:
            uinput, answer = lcmQuestion()
        case 3:
            uinput, answer = gcfxlcmQuestion()

    return printAnswerValidation(int(uinput), answer, answer)


def compareFractions():
    num1 = 1
    num2 = 1
    den1 = 1
    den2 = 1
    while den1 == 1 or den2 == 1 or den1 == den2 or abs(num1 / den1 - num2 / den2) > .1 or num1 == num2 or getgcf(num1,
                                                                                                                  den1) != 1 or getgcf(
            num2, den2) != 1:
        num1 = random.randint(1, 9)
        num2 = random.randint(1, 9)
        den1 = random.randint(2, 9)
        den2 = random.randint(2, 9)
        gcfOne = getgcf(num1, den1)
        gcfTwo = getgcf(num2, den2)
        num1 /= gcfOne
        num2 /= gcfTwo
        den1 /= gcfOne
        den2 /= gcfTwo
    if num1 / den1 > num2 / den2:
        answer = f"{int(num1)}/{int(den1)}"
    elif num2 / den2 > num1 / den1:
        answer = f"{int(num2)}/{int(den2)}"
    else:
        answer = "neither"
    uinput = better_frac_input(f"""Which is larger: 
{int(num1)}/{int(den1)} or {int(num2)}/{int(den2)}: """)

    return printAnswerValidation(uinput, answer, answer)


def differenceOfSquares():
    num1 = random.randint(11, 46)
    num2 = num1 + random.randint(1, 2) * 2
    answer = num2 * num2 - num1 * num1
    uinput = better_num_input(f"What is {num2} squared - {num1} squared? ")

    return printAnswerValidation(int(uinput), answer, answer)


def closeToHundred():
    type = random.randint(1, 2)
    if type == 1:
        num1 = random.randint(85, 99)
        num2 = random.randint(90, 99)
    if type == 2:
        num1 = random.randint(101, 115)
        num2 = random.randint(101, 110)
    answer = num1 * num2
    uinput = better_num_input(f"{num1} * {num2} = ")
    return printAnswerValidation(int(uinput), answer, answer)


def xAndyCubed():
    a = random.randint(1, 5)
    b = random.randint(1, 10)
    answer = b * b * b - 3 * a * b
    uinput = better_num_input(f"If x + y = {b} and xy = {a} then x cubed + y cubed is: ")

    return printAnswerValidation(int(uinput), answer, answer)


def divideFractions():
    num1 = 1
    num2 = 1
    den1 = 1
    den2 = 1
    while den1 == 1 or den2 == 1:
        num1 = random.randint(1, 9)
        num2 = random.randint(1, 9)
        den1 = random.randint(2, 9)
        den2 = random.randint(2, 9)
        gcfOne = getgcf(num1, den1)
        gcfTwo = getgcf(num2, den2)
        num1 /= gcfOne
        num2 /= gcfTwo
        den1 /= gcfOne
        den2 /= gcfTwo
    numFinal = num1 * den2
    denFinal = den1 * num2
    gcfFinal = getgcf(numFinal, denFinal)
    numFinal /= gcfFinal
    denFinal /= gcfFinal
    product = numFinal / denFinal
    uinput = better_frac_input(f"{int(num1)}/{int(den1)} ➗ {int(num2)}/{int(den2)} = ")

    if denFinal == 1:
        return printAnswerValidation(eval(uinput), product, int(numFinal))

    return printAnswerValidation(eval(uinput), product, f"{int(numFinal)}/{int(denFinal)}")


def stats():
    type = random.randint(1, 3)
    num1 = random.randint(1, 30)
    num2 = random.randint(1, 30)
    num3 = random.randint(1, 30)
    num4 = random.randint(1, 30)
    num5 = random.randint(1, 30)
    list = [num1, num2, num3, num4, num5]
    list.sort()
    # ---------
    match type:
        case 1:
            term = "range"
            answer = max(num1, num2, num3, num4, num5) - min(num1, num2, num3, num4, num5)
        case 2:
            term = "median"
            answer = list[2]
        case 3:
            term = "mean"
            answer = (num1 + num2 + num3 + num4 + num5) / 5
    uinput = better_frac_input(f"What is the {term} of {num1}, {num2}, {num3}, {num4}, and {num5}? ")

    return printAnswerValidation(eval(uinput), answer, answer)


def integralDivisorsQuestion():
    num = random.randint(6, 50) * 2
    answer = integralDivisors(num)
    uinput = better_num_input(f"{num} has how many integral divisors? ")

    return printAnswerValidation(int(uinput), answer, answer)


def logarithmQuestion():
    base = random.choice(logFactors)
    x = int(round(m.pow(base, random.randint(1, 5))))
    answer = round(m.log(x, base))
    uinput = better_num_input(f"What is log base {base} of {x}? ")
    """
 key = getkey()
    uinput = input(f"BUZZER PRESSED ({''.join(['player1' if key == player1Buzzer elif key == player2Buzzer 'player2'])}!) \n>> ")
    # https://replit.com/talk/ask/Python-How-do-I-without-pressing-enter/33815

 """

    return printAnswerValidation(int(uinput), answer, answer)


def sepDigits():
    dig1 = random.randint(1, 9)
    dig2 = random.randint(1, 9)
    dig3 = random.randint(0, 9)
    dig4 = random.randint(0, 9)
    dig5 = random.randint(0, 9)

    num1 = 100 * dig1 + dig3 + .1 * dig4
    num2 = 10 * dig2 + .01 * dig5
    answer = round(num1 + num2, 2)
    uinput = better_frac_input(f"{num1} + {num2} = ", decimal=True)
    return printAnswerValidation(float(uinput), answer, answer)


def xtoy1():
    x = random.randint(2, 10)
    z = random.randint(1, 10)
    type = random.randint(1, 3)
    match type:
        case 1:
            operation = "(y + 1)"
            z = random.randint(1, int(100 / x)) * x
            answer = z / x
        case 2:
            operation = "(y - 1)"
            answer = z * x
        case 3:
            operation = "(.5y)"
            answer = z * z
    uinput = better_num_input(f"If {x}^{operation} = {z}, what is {x}^y?: ")
    return printAnswerValidation(round(eval(uinput), 2), answer, answer)


def addCommonProducts():
    num1 = random.randint(5, 20)
    num2 = random.randint(3, 10) * 10
    num3 = random.randint(1, num2 - 1)
    num4 = num2 - num3
    answer = num4 * num1 + num3 * num1
    uinput = better_num_input(f"{num1} x {num3} + {num1} x {num4} = ")
    return printAnswerValidation(int(uinput), answer, answer)


def subsets():
    num1 = random.randint(1, 8)
    return 2 ** num1, num1


def properSubsets():
    num1, num2 = subsets()
    return num1 - 1, num2


def subsetsQuestion():
    type = random.randint(1, 2)
    match type:
        case 1:
            answer, numE = subsets()
            term = "subsets"
        case 2:
            answer, numE = properSubsets()
            term = "proper subsets"
    uinput = better_num_input(f"How many {term} does a {numE}-element set have?: ")
    return printAnswerValidation(int(uinput), answer, answer)


def multiplyOver37():
    num1 = random.randint(1, 9) * 111
    num2 = random.randint(1, 5)
    answer = int(num1 / 37 * num2)
    uinput = better_num_input(f"What is {num1} x {num2}/37?: ")
    return printAnswerValidation(int(uinput), answer, answer)


def orderOfOperationsQuestion():
    num1 = str(random.randint(1, 9)) + " "
    num2 = str(random.randint(1, 9)) + " "
    num3 = str(random.randint(1, 9)) + " "
    num4 = str(random.randint(1, 9)) + " "
    op1 = random.choice(operations) + " "
    op2 = random.choice(operations) + " "
    op3 = random.choice(operations) + " "
    answer = num1 + op1 + num2 + op2 + num3 + op3 + num4
    uinput = better_num_input(answer + "= ")
    answer = eval(answer)
    return printAnswerValidation(int(uinput), answer, answer)

# Needs some bug fixing
def decimalToFractions():
	type = random.randint(1,4)
	match type:
		case 1:
			# Non-repeating decimals
			denominator = random.choice(normBaseFractions)
			numerator = random.randint(1,denominator - 1)
			numerator, denominator = simplify(numerator, denominator)
			printt = str(round(numerator/denominator,3))
		case 2:
			a = random.randint(1,9)
			b = random.randint(1,9)
			printt = f"0.{a}{b}{a}{b}{a}{b}..."
			numerator, denominator = simplify(int(f"{a}{b}"),99)
			
		case 3:
			wType = random.randint(1,2)
			match wType:
				case 1:
					a = random.randint(1,9)
					b = random.randint(1,9)
					printt = f"0.{a}{b}{b}{b}{b}{b}..."
					numerator, denominator = simplify(int(f"{a}{b}") - a, 90)
				case 2:
					a = random.randint(1,9)
					b = random.randint(1,9)
					c = random.randint(1,9)
					printt = f"0.{a}{b}{c}{b}{c}{b}{c}..."
					numerator, denominator = simplify(int(f"{a}{b}{c}") - a, 990)
					
			
		case 4:
			a = random.randint(1,9)
			b = random.randint(1,9)
			c = random.randint(1,9)
			printt = f"0.{a}{b}{c}{a}{b}{c}..."
			numerator, denominator = simplify(int(f"{a}{b}{c}"), 999)	
	uinput = better_frac_input(f"What is {printt} as a fraction? ")
	pAnswer = f"{int(numerator)}/{int(denominator)}"
	return printAnswerValidation(eval(uinput),numerator/denominator,pAnswer)

def simplify(numerator, denominator):
	while getgcf(numerator,denominator) != 1:
		gcf = getgcf(numerator, denominator)
		numerator /= gcf
		denominator /= gcf
	return numerator, denominator

def fracToDec():
	denominator = random.choice(normBaseFractions)
	numerator = random.randint(1,denominator - 1)
	numerator, denominator = simplify(numerator, denominator)
	pAnswer = f"{int(numerator)}/{int(denominator)}"
	uinput = better_frac_input(f"What is {pAnswer} as a decimal? ")
	answer = numerator/denominator
	pAnswer = round(numerator/denominator,3)
	return printAnswerValidation(eval(uinput), answer,pAnswer)

def addOppositeFractions():
	numerator1 = 1
	denominator1 = 1
	while numerator1 == 1 or denominator1 == 1:
		numerator1, denominator1 = simplify(random.randint(2,9),random.randint(2,9))
	uinput = better_frac_input(f"{int(numerator1)}/{int(denominator1)} + {int(denominator1)}/{int(numerator1)} = 2 + ")
	ansNum, ansDem = simplify((numerator1 - denominator1) ** 2, (numerator1 * denominator1))
	pAnswer = f"{ansNum}/{ansDem}"
	answer = ansNum / ansDem
	return printAnswerValidation(eval(uinput),answer,pAnswer)