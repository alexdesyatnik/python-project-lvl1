from random import randint, choice


PROMPT = "What is the result of the expression?"


def make_question():
    op = choice(['+', '-', '*'])
    a = randint(1, 100)
    b = randint(1, 100)
    question = f"{a} {op} {b}"
    correct_answer = str(eval(question))
    return (question, correct_answer)
