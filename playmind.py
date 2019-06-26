#!/usr/bin/env python3

"""PlayMind.py

PlayMind is a command line game to practice your Math skills.

Train your mind doing mental calculations.
Operations supported: Addition, subtraction, multiplication and division.

By Ronny Yabar <ronny@kde.org>

"""

import operator
import time
import webbrowser
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


class PlayMindGame(object):
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
        """Round the result of the operation between two numbers."""
        result = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
        }[operation](num_a, num_b)

        return round(result, 1)

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
        """Start the timer and show the operations to calculate one by one."""
        start_time = time.perf_counter()
        operations = ['+', '-', '*', '/']
        for i in range(self.num_questions):
            num_a = self.get_random_num()
            num_b = self.get_random_num()
            if num_a < num_b:
                num_a, num_b = num_b, num_a
            operator_str = operations[self.operation - 1]
            result = self.get_result(operator_str, num_a, num_b)
            question = ' {0}/{1}:  {2} {3} {4} = '.format(
                i + 1, self.num_questions, num_a, operator_str, num_b
            )
            user_answer = get_positive_int(question)

            if result == user_answer:
                self.num_correct += 1
            else:
                self.num_incorrect += 1

        end_time = time.perf_counter()
        self.total_time = round(end_time - start_time, 2)
        self.show_highscores()

    def get_random_num(self):
        """Get a random integer number."""
        min_num = self.get_level_nums()[0]
        max_num = self.get_level_nums()[1]
        return randint(min_num, max_num)

    def get_level_nums(self):
        """Generate the limit numbers based on the level.

        Get a list with the minimun and maximum to generate random numbers.
            [10, 99]
            [100, 999]
            [1000, 9999]
            [10000, 99999]
            [100000, 999999]
            ...

        """
        start = 1
        limits = []
        for _ in range(self.level):
            start *= 10
        end = start*10 - 1

        limits.append(start)
        limits.append(end)
        return limits

    def show_highscores(self):
        """Show highscores like the time and number of correct answers."""
        print('\n\t\tHIGHSCORES')
        separators = ' {} | {} | {} | {} | {} | {}'
        headers = [
            'Operation', 'Level', 'Correct',
            'Incorrect', 'Total', 'Time'
        ]
        highscores = [
            OPERATIONS[self.operation - 1], LEVELS[self.level - 1],
            self.num_correct, self.num_incorrect,
            self.num_questions, self.total_time
        ]

        for i, _ in enumerate(highscores):
            len_header = len(headers[i])
            len_highscore = len(str(highscores[i]))
            if len_header < len_highscore:
                num_spaces = len_highscore - len_header
                spaces = ' ' * num_spaces
                headers[i] = headers[i] + spaces
            else:
                num_spaces = len_header - len_highscore
                spaces = ' ' * num_spaces
                highscores[i] = str(highscores[i]) + spaces

        print(separators.format(*headers))
        print(separators.replace('|', ' ').format(*highscores))
        self.check_win()

    def check_win(self):
        """Check if the player wins, then play a winning song."""
        if self.num_correct == self.num_questions:
            print('\n\t\tCONGRATULATIONS! YOU WIN.')
            youtube_url = 'https://www.youtube.com/watch?v=uxfrz6iQb9A'
            webbrowser.open(youtube_url)


def get_game_option(message, options):
    """Show a list of options based on the game question."""
    while True:
        print('{}: '.format(message))
        for i, option in enumerate(options):
            print(' {} {}'.format(i + 1, option))

        option = get_positive_int(' : ')
        if option <= len(options):
            break

    return option


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
