#!/usr/bin/env python

from brain_games.cli import play_game
from brain_games.games import gcd_game


def main():
    play_game(gcd_game)


if __name__ == "__main__":
    main()
