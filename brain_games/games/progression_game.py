from random import randint


PROMPT = "What number is missing in the progression?"


def make_question():
    progr_start = randint(1, 20)
    progr_length = randint(5, 10)
    progr_step = randint(1, 10)
    missing_position = randint(0, progr_length - 1)
    progression = list(range(progr_start,
                             progr_start + progr_step * progr_length - 1,
                             progr_step))
    question = " ".join(str(n) if i != missing_position else ".."
                        for i, n in enumerate(progression))
    correct_answer = str(progression[missing_position])
    return (question, correct_answer)
