#!/usr/bin/env python

from brain_games.cli import play_game
from brain_games.games import calc_game


def main():
    play_game(calc_game.PROMPT, calc_game.make_question)


if __name__ == "__main__":
    main()
