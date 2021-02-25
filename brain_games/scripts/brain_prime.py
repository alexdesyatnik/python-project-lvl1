#!/usr/bin/env python

from brain_games.cli import play_game
from brain_games.games import prime_game


def main():
    play_game(prime_game)


if __name__ == "__main__":
    main()
