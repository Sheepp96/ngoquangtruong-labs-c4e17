from random import *
from eval import *

def generate_quiz():
    # Hint: Return [x, y, op, result]

    m = randint(0, 10)
    n = randint(0, 10)

    op = choice(["+", "-", "*", "/"])

    result = eval.calc(m, n, op)
    error = choice([-1, 0, 0, 1])
    display_result = result + error

    return(m, n, op, result)


def check_answer(m, n, op, result, user_choice):

    if display_result == result:
        if user_choice == True:
            return True
        else:
            return False
    else:
        if user_choice == True:
            return False
        else:
            return True
