#!/usr/bin/env python

from brain_games.cli import play_game
from brain_games.games import even_game


def main():
    play_game(even_game)


if __name__ == "__main__":
    main()
