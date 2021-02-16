#!/usr/bin/env python

from brain_games.cli import play_even_game, welcome_user


def main():
    name = welcome_user()
    play_even_game(name)
