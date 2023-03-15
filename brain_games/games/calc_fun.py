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
        if answer.strip() == str(ch):
            j += 1
            print ('Correct!')
        else:
            j = 0
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{ch}'.")


def greatest_divisor():
    print('Find the greatest common divisor of given numbers.')
    j = 0
    while j < 3:
        ch1 = randint(1, 100)
        ch2 = randint(1, 100)
        print(f'Question: {ch1} {ch2}')
        while ch1 != 0 and ch2 != 0:
            if ch1 > ch2:
                ch1 = ch1 % ch2
            else:
                ch2 = ch2 % ch1
        ch = ch1 + ch2
        answer = input('Your answer: ')
        if answer.strip() == str(ch):
            j += 1
            print('Correct!')
        else:
            j = 0
            print(
                f"'{answer}' is wrong answer ;(. Correct answer was '{ch}'.")
