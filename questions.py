import random
import math as m
from utils import better_num_input, better_frac_input
# noinspection PyPep8Naming
from colorama import init as colorama_init, Fore as C, Style

colorama_init(True)

RESET = Style.RESET_ALL

multiplyFactors = [25, 25, 25, 75, 75, 101, 11, 11, 11, 111, 101]
remainderFactors = [3, 3, 3, 3, 4, 4, 8, 9, 9, 9, 11, 11, 11]
logFactors = [2, 4, 5, 10]
operations = ["*", "+", "-"]
normBaseFractions = [2, 4, 5, 8, 10, 20, 25, 40]


def print_answer_validation(uinput, ans, return_ans, decimal=False):
    """Returns whether the question was answered correctly"""
    # TODO: Have an option for multiple attempts, skips the question if pressing enter with empty answer
    decimal_correct = True
    if decimal and type(ans) == float :
        dec_ans = [*str(uinput)]
        if dec_ans[0] == "0":
            decimal_correct = False
        dec_ans = [*str(ans)]
        length = len(dec_ans)
        return_ans = ""
        if dec_ans[0] == "0":
            for i in range(1,length):
                return_ans += dec_ans[i]
        else:
            for i in range(0,length):
                return_ans += dec_ans[i]
        ans = return_ans
    if str(uinput) == str(ans) and decimal_correct:
        print(f"{C.GREEN}✅ Correct")
        return True
    else:
        print(f"{C.RED}❌ Incorrect.{RESET} Answer is {return_ans}")
        return False


def multiply_by(rand_factor=None, diff_types=False):
    if rand_factor is None:
        factor = random.choice(multiplyFactors)
    else:
        factor = rand_factor
    if diff_types:
        multiple = random.randint(11, 30)
    else:
        multiple = random.randint(3, 25) * 4
    answer = better_num_input(f"{multiple} x {factor} = ")
    return print_answer_validation(answer, str(int(multiple * factor)), str(int(multiple * factor)))


def divide_by(factor):
    """divides a thing"""
    multiplier = random.randint(1, 20)
    product = multiplier * factor
    answer = better_num_input(f"{product} ➗ {factor} = ")
    return print_answer_validation(answer, str(int(product / factor)), str(int(product / factor)))


def multiply_fractions():
    num1 = 1
    num2 = 1
    den1 = 1
    den2 = 1
    while den1 == 1 or den2 == 1:
        num1 = random.randint(1, 9)
        num2 = random.randint(1, 9)
        den1 = random.randint(2, 9)
        den2 = random.randint(2, 9)
        gcf1 = get_gcf(num1, den1)
        gcf2 = get_gcf(num2, den2)
        num1 /= gcf1
        num2 /= gcf2
        den1 /= gcf1
        den2 /= gcf2
    num_final = num1 * num2
    den_final = den1 * den2
    gcf_final = get_gcf(num_final, den_final)
    num_final /= gcf_final
    den_final /= gcf_final
    uinput = better_frac_input(f"{int(num1)}/{int(den1)} x {int(num2)}/{int(den2)} = ")
    if den_final == 1:
        return print_answer_validation(uinput, int(num_final), int(num_final))
    return print_answer_validation(uinput,f"{int(num_final)}/{int(den_final)}", f"{int(num_final)}/{int(den_final)}")


def get_gcf(a, b):
    if b == 0:
        return abs(a)
    else:
        return get_gcf(b, a % b)


def get_lcm(a, b):
    return a * b / get_gcf(a, b)


def integral_divisors(a):
    num = 0
    for i in range(1, a + 1):
        if a % i == 0:
            num += 1
    return num


def centered_around_third():
    factor = random.randint(1, 4)
    num = random.randint(0, 9) * 10 + 5
    uinput = better_num_input(f"{num - factor} x {num + factor} = ")
    answer = (num - factor) * (num + factor)
    return print_answer_validation(eval(uinput), answer, answer)


def square_number(easy=False):
    num = None
    if easy:
        num_t = random.randint(1, 2)
        match num_t:
            case 1:
                num = random.randint(11, 30)
            case 2:
                num = random.randint(41, 60)
    else:
        num = random.randint(11, 60)
    answer = num * num
    uinput = better_num_input(f"What is {num} squared? ")
    return print_answer_validation(int(uinput), answer, answer)


def cube_number():
    num = random.randint(2, 15)
    answer = num * num * num
    uinput = better_num_input(f"What is {num} cubed? ")
    return print_answer_validation(int(uinput), answer, answer)


def square_root_number():
    num = random.randint(11, 100)
    answer = num
    uinput = better_num_input(f"What is the square root of {num * num}? ")
    return print_answer_validation(int(uinput), answer, answer)


def cube_root_number():
    num = random.randint(11, 100)
    answer = num
    uinput = better_num_input(f"What is the cube root of {num * num * num}? ")

    return print_answer_validation(int(uinput), answer, answer)


def difference_of_reverses(digits):
    if digits == 3:
        num1 = random.randint(1, 9)
        num2 = random.randint(1, 9)
        num3 = random.randint(1, 9)
        answer = (100 * num1 + 10 * num2 + num3) - (100 * num3 + 10 * num2 + num1)
        uinput = better_frac_input(f"{num1}{num2}{num3} - {num3}{num2}{num1} = ")
        return print_answer_validation(int(uinput), answer, answer)

    if digits == 4:
        num1 = random.randint(1, 9)
        num2 = random.randint(1, 9)
        answer = (1000 * num1 + num2) - (1000 * num2 + num1)
        uinput = int(better_num_input(f"{num1}00{num2} - {num2}00{num1} = "))
        return print_answer_validation(int(uinput), answer, answer)


def lcm_question():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    answer = int(get_lcm(num1, num2))
    uinput = better_num_input(f"lcm({num1},{num2}) = ")

    return uinput, answer


def gcf_question():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)

    answer = get_gcf(num1, num2)
    uinput = better_num_input(f"gcf({num1},{num2}) = ")

    return uinput, answer


def gcf_xlcm_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    answer = num1 * num2
    uinput = better_num_input(f"gcf({num1},{num2}) x lcm({num1},{num2}) = ")

    return uinput, answer


def add_squares(q_type):
    uinput, answer = None, None
    if q_type == 1:
        num1 = random.randint(1, 20)
        uinput = better_num_input(f"{num1} squared + {num1 * 3} squared? ")
        answer = num1 * num1 * 10

    if q_type == 2:
        dig11 = random.randint(1, 9)
        dig12 = random.randint(1, 9)
        dig21 = dig12 - 1
        dig22 = 10 - dig11
        num1 = 10 * dig11 + dig12
        num2 = 10 * dig21 + dig22
        uinput = better_num_input(f"{num1} squared + {num2} squared? ")
        answer = num1 * num1 + num2 * num2
    return print_answer_validation(int(uinput), answer, answer)


def remainder():
    num1 = random.randint(1, 100000)
    num2 = random.choice(remainderFactors)
    answer = num1 % num2
    uinput = better_num_input(f"Remainder of {num1} / {num2} = ")

    return print_answer_validation(int(uinput), answer, answer)


def gcf_lcm_question():
    uinput, answer = None, None
    q_type = random.randint(1, 3)
    match q_type:
        case 1:
            uinput, answer = gcf_question()
        case 2:
            uinput, answer = lcm_question()
        case 3:
            uinput, answer = gcf_xlcm_question()

    return print_answer_validation(int(uinput), answer, answer)


def compare_fractions():
    num1 = 1
    num2 = 1
    den1 = 1
    den2 = 1
    while den1 == 1 \
            or den2 == 1 \
            or den1 == den2 \
            or abs(num1 / den1 - num2 / den2) > .1 \
            or num1 == num2 \
            or get_gcf(num1, den1) != 1 \
            or get_gcf(num2, den2) != 1:
        num1 = random.randint(1, 9)
        num2 = random.randint(1, 9)
        den1 = random.randint(2, 9)
        den2 = random.randint(2, 9)
        gcf1 = get_gcf(num1, den1)
        gcf2 = get_gcf(num2, den2)
        num1 /= gcf1
        num2 /= gcf2
        den1 /= gcf1
        den2 /= gcf2
    if num1 / den1 > num2 / den2:
        answer = f"{int(num1)}/{int(den1)}"
    elif num2 / den2 > num1 / den1:
        answer = f"{int(num2)}/{int(den2)}"
    else:
        answer = "neither"
    uinput = better_frac_input(f"""Which is larger: 
{int(num1)}/{int(den1)} or {int(num2)}/{int(den2)}: """)

    return print_answer_validation(uinput, answer, answer)


def difference_of_squares():
    num1 = random.randint(11, 46)
    num2 = num1 + random.randint(1, 2) * 2
    answer = num2 * num2 - num1 * num1
    uinput = better_num_input(f"What is {num2} squared - {num1} squared? ")

    return print_answer_validation(int(uinput), answer, answer)


def close_to_hundred():
    num1, num2 = None, None
    q_type = random.randint(1, 2)
    if q_type == 1:
        num1 = random.randint(85, 99)
        num2 = random.randint(90, 99)
    if q_type == 2:
        num1 = random.randint(101, 115)
        num2 = random.randint(101, 110)
    answer = num1 * num2
    uinput = better_num_input(f"{num1} * {num2} = ")
    return print_answer_validation(int(uinput), answer, answer)


def x_and_y_cubed():
    a = random.randint(1, 5)
    b = random.randint(1, 10)
    answer = b * b * b - 3 * a * b
    uinput = better_num_input(f"If x + y = {b} and xy = {a} then x cubed + y cubed is: ")

    return print_answer_validation(int(uinput), answer, answer)


def divide_fractions():
    num1 = 1
    num2 = 1
    den1 = 1
    den2 = 1
    while den1 == 1 or den2 == 1:
        num1 = random.randint(1, 9)
        num2 = random.randint(1, 9)
        den1 = random.randint(2, 9)
        den2 = random.randint(2, 9)
        gcf1 = get_gcf(num1, den1)
        gcf2 = get_gcf(num2, den2)
        num1 /= gcf1
        num2 /= gcf2
        den1 /= gcf1
        den2 /= gcf2
    num_final = num1 * den2
    den_final = den1 * num2
    gcf_final = get_gcf(num_final, den_final)
    num_final /= gcf_final
    den_final /= gcf_final
    uinput = better_frac_input(f"{int(num1)}/{int(den1)} ➗ {int(num2)}/{int(den2)} = ")

    if den_final == 1:
        return print_answer_validation(uinput, int(num_final), int(num_final))

    return print_answer_validation(uinput, f"{int(num_final)}/{int(den_final)}", f"{int(num_final)}/{int(den_final)}")


def stats():
    q_type = random.randint(1, 3)
    num1 = random.randint(1, 30)
    num2 = random.randint(1, 30)
    num3 = random.randint(1, 30)
    num4 = random.randint(1, 30)
    num5 = random.randint(1, 30)
    num_list = [num1, num2, num3, num4, num5]
    num_list.sort()
    # ---------
    term, answer = None, None
    match q_type:
        case 1:
            term = "range"
            answer = max(num1, num2, num3, num4, num5) - min(num1, num2, num3, num4, num5)
        case 2:
            term = "median"
            answer = num_list[2]
        case 3:
            term = "mean"
            answer = (num1 + num2 + num3 + num4 + num5) / 5
    uinput = better_frac_input(f"What is the {term} of {num1}, {num2}, {num3}, {num4}, and {num5}? ")

    return print_answer_validation(eval(uinput), answer, answer,decimal=True)


def integral_divisors_question():
    num = random.randint(6, 50) * 2
    answer = integral_divisors(num)
    uinput = better_num_input(f"{num} has how many integral divisors? ")

    return print_answer_validation(int(uinput), answer, answer)


def logarithm_question():
    base = random.choice(logFactors)
    x = int(round(m.pow(base, random.randint(1, 5))))
    answer = round(m.log(x, base))
    uinput = better_num_input(f"What is log base {base} of {x}? ")
    return print_answer_validation(int(uinput), answer, answer)


def sep_digits():
    dig1 = random.randint(1, 9)
    dig2 = random.randint(1, 9)
    dig3 = random.randint(0, 9)
    dig4 = random.randint(0, 9)
    dig5 = random.randint(0, 9)

    num1 = 100 * dig1 + dig3 + .1 * dig4
    num2 = 10 * dig2 + .01 * dig5
    answer = round(num1 + num2, 2)
    uinput = better_frac_input(f"{num1} + {num2} = ", decimal=True)
    return print_answer_validation(float(uinput), answer, answer)


def xtoy1():
    x = random.randint(2, 10)
    z = random.randint(1, 10)
    q_type = random.randint(1, 3)
    operation, answer = None, None
    match q_type:
        case 1:
            operation = "(y + 1)"
            z = random.randint(1, int(100 / x)) * x
            answer = int(z / x)
        case 2:
            operation = "(y - 1)"
            answer = z * x
        case 3:
            operation = "(.5y)"
            answer = z * z
    uinput = better_num_input(f"If {x}^{operation} = {z}, what is {x}^y?: ")
    return print_answer_validation(uinput, answer, answer)


def add_common_products():
    num1 = random.randint(5, 20)
    num2 = random.randint(3, 10) * 10
    num3 = random.randint(1, num2 - 1)
    num4 = num2 - num3
    answer = num4 * num1 + num3 * num1
    uinput = better_num_input(f"{num1} x {num3} + {num1} x {num4} = ")
    return print_answer_validation(int(uinput), answer, answer)


def subsets():
    num1 = random.randint(1, 8)
    return 2 ** num1, num1


def proper_subsets():
    num1, num2 = subsets()
    return num1 - 1, num2


def subsets_question():
    q_type = random.randint(1, 2)
    term, answer, num_e = None, None, None
    match q_type:
        case 1:
            answer, num_e = subsets()
            term = "subsets"
        case 2:
            answer, num_e = proper_subsets()
            term = "proper subsets"
    uinput = better_num_input(f"How many {term} does a {num_e}-element set have?: ")
    return print_answer_validation(int(uinput), answer, answer)


def multiply_over_37():
    num1 = random.randint(1, 9) * 111
    num2 = random.randint(1, 5)
    answer = int(num1 / 37 * num2)
    uinput = better_num_input(f"What is {num1} x {num2}/37?: ")
    return print_answer_validation(int(uinput), answer, answer)


def order_of_operations_question():
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
    return print_answer_validation(int(uinput), answer, answer)


# Needs some bug fixing
def decimal_to_fractions():
    q_type = random.randint(1, 4)
    numerator, denominator, printt = None, None, None
    match q_type:
        case 1:
            # Non-repeating decimals
            denominator = random.choice(normBaseFractions)
            numerator = random.randint(1, denominator - 1)
            numerator, denominator = simplify(numerator, denominator)
            printt = str(round(numerator / denominator, 3))
        case 2:
            a = random.randint(1, 9)
            b = random.randint(1, 9)
            printt = f"0.{a}{b}{a}{b}{a}{b}..."
            numerator, denominator = simplify(int(f"{a}{b}"), 99)

        case 3:
            w_type = random.randint(1, 2)
            match w_type:
                case 1:
                    a = random.randint(1, 9)
                    b = random.randint(1, 9)
                    printt = f"0.{a}{b}{b}{b}{b}{b}..."
                    numerator, denominator = simplify(int(f"{a}{b}") - a, 90)
                case 2:
                    a = random.randint(1, 9)
                    b = random.randint(1, 9)
                    c = random.randint(1, 9)
                    printt = f"0.{a}{b}{c}{b}{c}{b}{c}..."
                    numerator, denominator = simplify(int(f"{a}{b}{c}") - a, 990)

        case 4:
            a = random.randint(1, 9)
            b = random.randint(1, 9)
            c = random.randint(1, 9)
            printt = f"0.{a}{b}{c}{a}{b}{c}..."
            numerator, denominator = simplify(int(f"{a}{b}{c}"), 999)
    uinput = better_frac_input(f"What is {printt} as a fraction? ")
    p_answer = f"{int(numerator)}/{int(denominator)}"
    return print_answer_validation(uinput, f"{int(numerator)}/{int(denominator)}", p_answer)


def simplify(numerator, denominator):
    while get_gcf(numerator, denominator) != 1:
        gcf = get_gcf(numerator, denominator)
        numerator /= gcf
        denominator /= gcf
    return numerator, denominator


def frac_to_dec():
    denominator = random.choice(normBaseFractions)
    numerator = random.randint(1, denominator - 1)
    numerator, denominator = simplify(numerator, denominator)
    p_answer = f"{int(numerator)}/{int(denominator)}"
    uinput = better_frac_input(f"What is {p_answer} as a decimal? ")
    answer = numerator / denominator
    p_answer = round(numerator / denominator, 3)
    return print_answer_validation(uinput, answer, p_answer, decimal=True)


def add_opposite_fractions():
    numerator1 = 1
    denominator1 = 1
    while numerator1 == 1 or denominator1 == 1:
        numerator1, denominator1 = simplify(random.randint(2, 9), random.randint(2, 9))
    uinput = better_frac_input(f"(Proper/Improper Fraction) {int(numerator1)}/{int(denominator1)} + {int(denominator1)}/{int(numerator1)} = 2 + ")
    ans_num, ans_dem = simplify((numerator1 - denominator1) ** 2, (numerator1 * denominator1))
    p_answer = f"{int(ans_num)}/{int(ans_dem)}"
    answer = p_answer
    return print_answer_validation(uinput, answer, p_answer)

    
# Takes a number from any base and converts it to base ten.
def convert_to_base_10(num, base):
    num = [*str(num)]
    answer = 0
    for i in range(-1, -1 * len(num)-1, -1):
        answer += int(num[i]) * (base ** (i * -1 - 1))
    return answer


def convert_from_base_10(num, base): # 15, 7 
    answer = ""
    while num > 0:
        i = 0
        while num >= base ** i:
            i += 1
        i -= 1 # 1 | 0
        digit = 0
        while num >= base ** i:
            num = num - (base ** i)
            digit += 1
        answer += str(digit)
    return int(answer)

    
def convert_to_base_10_question():
    number = random.randint(11,99)
    base = random.randint(2,9)
    answer = convert_to_base_10(number,base)
    uinput = better_num_input(f"What is {number} base {base} in base 10? ")
    print_answer_validation(answer,uinput,answer)

def convert_from_base_10_question():
    number = random.randint(11,300)
    base = random.randint(2,9)
    answer = convert_from_base_10(number,base)
    uinput = better_num_input(f"What is {number} base 10 in base {base}? ")
    print_answer_validation(answer,uinput,answer)