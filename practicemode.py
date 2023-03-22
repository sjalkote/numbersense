
import questions
import random

from pick import pick

Groups = ["Basic Operations", "Powers", "Parts of the Whole", "Data and Algebra"]
GroupsOne = ["Multiplying by 25", "Multiplying by 75", "Multiplying by 101", "Multiplying by 11", "Difference of Reverses",  "Multiplying Two Numbers Centered Around a Third", "Remainders","Adding with Common Products",  "Multiplying Numbers Close to 100", "Adding with digits and 0's", "Multiplying over 37"]
GroupsTwo = ["Squaring Numbers", "Cubing Numbers", "Square Rooting Numbers", "Cube Rooting Numbers", "Adding Squares Type One", "Adding Squares Type Two", "Difference of squares", "Logarithms"]
GroupsThree = ["Multiplying Fractions", "Compare Fractions", "Dividing Fractions", "Adding Opposite Fractions", "Decimal to Fractions", "Fractions to Decimals"]
GroupsFour = ["GCF and LCM", "Mean, Median, and Range", "Integral Divisors", "Subsets", "Order of Operations",
                "x to y +/- 1", "x and y cubed Algebra", "Converting to base 10", "Converting from base 10"]

def choose_type():
    category, category_index = pick(Groups, "What topic?", indicator='👉', default_index=0)
    match category_index:
        case 0:
            category1, category1_index = pick(GroupsOne, "What topic?", indicator='👉', default_index=0)
            match category1_index:
                case 0:
                    return questions.multiply_by, 25
                case 1:
                    return questions.multiply_by, 75
                case 2:
                    return questions.multiply_by, 101
                case 3:
                    return questions.multiply_by, 11
                case 4:
                    return questions.difference_of_reverses, None
                case 5:
                    return questions.centered_around_third, None
                case 6:
                    return questions.remainder, None
                case 7:
                    return questions.add_common_products, None
                case 8:
                    return questions.close_to_hundred, None
                case 9: 
                    return questions.multiply_over_37, None
        case 1:
            category2, category2_index = pick(GroupsTwo, "What topic?", indicator='👉', default_index=0)
            match category2_index:
                case 0:
                    return questions.square_number, None
                case 1:
                    return questions.cube_number, None
                case 2:
                    return questions.square_root_number, None
                case 3:
                    return questions.cube_root_number, None
                case 4:
                    return questions.add_squares, 1
                case 5:
                    return questions.add_squares, 2
                case 6:
                    return questions.difference_of_squares, None
                case 7:
                    return questions.logarithm_question, None
        case 2:
            category3, category3_index = pick(GroupsThree, "What topic?", indicator='👉', default_index=0)
            match category3_index:
                case 0:
                    return questions.multiply_fractions, None
                case 1:
                    return questions.compare_fractions, None
                case 2:
                    return questions.divide_fractions, None
                case 3:
                    return questions.add_opposite_fractions, None
                case 4:
                    return questions.decimal_to_fractions, None
                case 5:
                    return questions.frac_to_dec, None
        case 3:
            category4, category4_index = pick(GroupsFour, "What topic?", indicator='👉', default_index=0)
            match category4_index:
                case 0:
                    return questions.gcf_xlcm_questions, None
                case 1:
                    return questions.stats, None
                case 2:
                    return questions.integral_divisors_question, None
                case 3:
                     return questions.subsets_question, None
                case 4:
                    return questions.order_of_operations_question, None
                case 5:
                    return questions.xtoy1, None
                case 6:
                    return questions.x_and_y_cubed, None
                case 7:
                    return questions.convert_to_base_10_question, None
                case 8:
                    return questions.convert_from_base_10_question, None
def practiceMode(list):
    question_func = list[0]
    type = list[1]
    num_correct = 0
    num_questions = input("How many questions? >> ")
    while not num_questions.isnumeric():
        num_questions = input("Invalid input. How many questions? >> ")
    num_questions = int(num_questions)
    if question_func.__name__ != questions.divide_by.__name__ and question_func.__name__ != questions.add_squares.__name__ and question_func.__name__ != questions.difference_of_reverses.__name__ and question_func.__name__ != questions.multiply_by.__name__ :
        for i in range(num_questions):
            if question_func():
                num_correct += 1
    elif question_func.__name__ == questions.divide_by.__name__:
        for i in range(num_questions):
            if question_func(type):
                num_correct += 1
    elif question_func.__name__ == questions.difference_of_reverses.__name__:
        for i in range(num_questions):
            if question_func(random.randint(3,4)):
                num_correct += 1
    elif question_func.__name__ == questions.add_squares.__name__:
        for i in range(num_questions):
            if question_func(type):
                num_correct += 1
    elif question_func.__name__ == questions.multiply_by.__name__:
        for i in range(num_questions):
            if question_func(type):
                num_correct += 1
    return num_questions, num_correct
