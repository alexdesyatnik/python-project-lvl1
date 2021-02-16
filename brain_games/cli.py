import prompt
from random import randint


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def even_game_guess():
    """Makes a random integer, asks used if it's even, checks the answer"""
    number = randint(1, 100)
    correct_answer = "yes" if number % 2 == 0 else "no"
    print(f"Question: {number}")
    answer = prompt.string("Your answer: ").lower()
    result = answer == correct_answer
    if result:
        print("Correct!")
    else:
        print(f"'{answer}' is wrong answer ;(. "
              + f"Correct answer was '{correct_answer}'.")
    return result


def play_even_game(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(3):
        if not even_game_guess():
            print(f"Let's try again, {name}!")
            break
    else:
        print(f"Congratulations, {name}!")
