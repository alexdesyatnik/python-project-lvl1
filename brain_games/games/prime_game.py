from random import randint


def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


PROMPT = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def make_question():
    a = randint(1, 1000)
    question = a
    correct_answer = "yes" if is_prime(a) else "no"
    return (question, correct_answer)
