from random import randint
from math import gcd


PROMPT = "Find the greatest common divisor of given numbers."


def make_question():
    a = randint(1, 100)
    b = randint(1, 100)
    question = f"{a} {b}"
    correct_answer = str(gcd(a, b))
    return (question, correct_answer)
