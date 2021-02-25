from random import randint


PROMPT = 'Answer "yes" if the number is even, otherwise answer "no".'


def make_question():
    """Generate a question and a correct answer"""
    number = randint(1, 100)
    correct_answer = "yes" if number % 2 == 0 else "no"
    return (number, correct_answer)
