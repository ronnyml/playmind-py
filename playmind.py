#!/usr/bin/env python3

"""PlayMind.py

PlayMind is a command line game to practice your Math skills.

Train your mind doing mental calculations.
Operations supported: Addition, subtraction, multiplication and division.

By Ronny Yabar <ronny@kde.org>

"""

import operator
import time
from random import randint

OPERATIONS = [
    'Addition',
    'Substraction',
    'Multiplication',
    'Division [1 decimal]'
]

LEVELS = [
    'Easy',
    'Medium',
    'Hard',
    'Super Hard',
    'Difficult'
]

OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}


class PlayMindGame:
    """Base class definition of the game."""

    def __init__(self, operation, level, num_questions):
        self.operation = operation
        self.level = level
        self.num_questions = num_questions
        self.num_correct = 0
        self.num_incorrect = 0
        self.total_time = 0

    @staticmethod
    def get_result(operation, num_a, num_b):
        """Perform the operation and round the result."""
        return round(OPERATORS[operation](num_a, num_b), 1)

    def init_game(self):
        """Ask the user if ready to start the game."""
        ready = input('\n Are you ready to start? y/n: ')
        if ready.strip().lower() == 'y':
            self.start_game()
        elif ready.strip.lower() == 'n':
            exit('Goodbye!')
        else:
            print('Choose y or n')

    def start_game(self):
        """Run the game by generating questions and recording scores."""
        start_time = time.perf_counter()
        operations = ['+', '-', '*', '/']
        operator_str = operations[self.operation - 1]

        for i in range(1, self.num_questions + 1):
            num_a, num_b = sorted([self.get_random_num(), self.get_random_num()], reverse=True)
            result = self.get_result(operator_str, num_a, num_b)
            question = f' {i}/{self.num_questions}:  {num_a} {operator_str} {num_b} = '
            user_answer = get_positive_int(question)

            if result == user_answer:
                self.num_correct += 1
            else:
                self.num_incorrect += 1

        self.total_time = round(time.perf_counter() - start_time, 2)
        self.show_highscores()

    def get_random_num(self):
        """Generate a random number within the level range."""
        min_num, max_num = self.get_level_nums()
        return randint(min_num, max_num)

    def get_level_nums(self):
        """Generate the range of numbers based on the level..

        Get a list with the minimun and maximum to generate random numbers.
            [10, 99]
            [100, 999]
            [1000, 9999]
            [10000, 99999]
            [100000, 999999]
            ...

        """
        start = 10 ** (self.level - 1)
        end = 10 ** self.level - 1
        return start, end

    def show_highscores(self):
        """Display highscores in a formatted table."""
        print('\n\t\tHIGHSCORES')
        headers = ['Operation', 'Level', 'Correct', 'Incorrect', 'Total', 'Time']
        highscores = [
            OPERATIONS[self.operation - 1], LEVELS[self.level - 1],
            self.num_correct, self.num_incorrect,
            self.num_questions, self.total_time
        ]

        # Print header row
        print(" | ".join(header.ljust(12) for header in headers))
        # Print scores
        print(" | ".join(str(score).ljust(12) for score in highscores))
        self.check_win()

    def check_win(self):
        """Check if the player wins, then play a winning song."""
        if self.num_correct == self.num_questions:
            print('\n\t\tCONGRATULATIONS! YOU WIN.')


def get_game_option(message, options):
    """Prompt user to select an option from a list."""
    while True:
        print(f'{message}:')
        for i, option in enumerate(options, 1):
            print(f' {i}. {option}')
        choice = get_positive_int('Choose an option: ')
        if 1 <= choice <= len(options):
            return choice
        print('Invalid choice. Please select a valid option.')


def get_positive_int(option):
    """Validate and return a positive integer number."""
    while True:
        try:
            response_int = int(input(option))
        except ValueError:
            print('\n\n Not a valid option. Please, choose a number.')
            continue
        except KeyboardInterrupt:
            exit('\n\n Game Interrupted, Quitting.')

        if response_int <= 0:
            print('\n\n Not a valid number. It should be positive.')
            continue
        else:
            break
    return response_int


def main():
    """Set up and choose game options."""
    print('\n\t\tPLAYMIND')
    operation = get_game_option('\n\tChoose the operation', OPERATIONS)
    level = get_game_option('\n\tChoose the level', LEVELS)
    num_questions = get_positive_int('\n How many questions? (5, 10, 100): ')
    playmind = PlayMindGame(operation, level, num_questions)
    playmind.init_game()


if __name__ == '__main__':
    main()
