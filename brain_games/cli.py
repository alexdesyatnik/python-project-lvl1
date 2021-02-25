import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def ask_question(question, correct_answer):
    """Asks user a question and check the answer"""
    print(f"Question: {question}")
    answer = prompt.string("Your answer: ").lower()
    result = answer == correct_answer
    if result:
        print("Correct!")
    else:
        print(f"'{answer}' is wrong answer ;(. "
              + f"Correct answer was '{correct_answer}'.")
    return result


def play_game(game_module):
    username = welcome_user()
    print(game_module.PROMPT)
    MAX_GAME_ROUNDS = 3
    for _ in range(MAX_GAME_ROUNDS):
        if not ask_question(*game_module.make_question()):
            print(f"Let's try again, {username}!")
            break
    else:
        print(f"Congratulations, {username}!")
