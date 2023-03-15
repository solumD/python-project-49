#!/usr/bin/env python3
from random import randint, choice


def start_round():
    print('What is the result of the expression?')
    j = 0
    while j < 3:
        ch1 = randint(0, 100)
        ch2 = randint(0, 100)
        op = choice('+-*')
        if op == '*':
            print(f'Question: {ch1} * {ch2}')
            ch = ch1 * ch2
        elif op == '+':
            print(f'Question: {ch1} + {ch2}')
            ch = ch1 + ch2
        else:
            print(f'Question: {ch1} - {ch2}')
            ch = ch1 - ch2
        answer = input('Your answer: ')
        if int(answer) == ch:
            j += 1
            print ('Correct!')
        else:
            j = 0
            print(f"'{int(answer)}' is wrong answer ;(. Correct answer was '{ch}'.")
