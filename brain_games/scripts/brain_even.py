#!/usr/bin/env python3
from ..cli import welcome_user
from random import randint


def main():
    print('Welcome to the Brain Games!')
    n = welcome_user()
    if start_round(n) == 1:
        goodbye(n)


def start_round(arg):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    j = 0
    while j < 3:
        ch = randint(0, 100)
        diff = ch % 2
        print(f'Question: {ch}')
        answer = input('Your answer: ')
        if diff == 1 and answer == 'no':
            j += 1
            print('Correct!')
        if diff == 0 and answer == 'yes':
            j += 1
            print('Correct!')
        if diff == 1 and answer != 'no':
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.")
            print(f"Let's try again, {arg}!")
            j = 3
            return 0
        if diff == 0 and answer != 'yes':
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.")
            print(f"Let's try again, {arg}!")
            j = 3
            return 0
    return 1


def goodbye(arg):
    return print(f'Congratulations, {arg}!')


if __name__ == '__main__':
    main()
