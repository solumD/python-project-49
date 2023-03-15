#!/usr/bin/env python3
from random import randint, choice


def start_round(arg):
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
            j = 3
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{ch}'.")
            print(f"Let's try again, {arg}!")
            return 0
    return 1


def greatest_divisor(arg):
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
            j = 3
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{ch}'.")
            print(f"Let's try again, {arg}!")
            return 0
    return 1


def ch_in_prog(arg):
    print('What number is missing in the progression?')
    j = 0
    while j < 3:
        ch1 = randint(0, 10)
        ch2 = randint(50, 60)
        sh = randint(5, 10)
        numbers = list()
        for i in range(ch1, ch2, sh):
            numbers.append(i)
        cof = randint(0, len(numbers) - 1)
        ch = numbers.pop(cof)
        numbers.insert(cof, '..')
        print('Question:', *numbers)
        answer = input('Your answer: ')
        if answer.strip() == str(ch):
            j += 1
            print('Correct!')
        else:
            j = 3
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{ch}'.")
            print(f"Let's try again, {arg}!")
            return 0
    return 1


def ch_prime(arg):
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    j = 0
    while j < 3:
        ch = randint(0, 50)
        k = 0
        for i in range(2, ch // 2 + 1):
            if ch % i == 0:
                k = k + 1
        print(f'Question: {ch}')
        answer = input('Your answer: ')
        if k <= 0 and answer == 'yes':
            print('Correct!')
            j += 1
        if k > 0 and answer == 'no':
            print('Correct!')
            j += 1
        if k > 0 and answer != 'no':
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.")
            print(f"Let's try again, {arg}!")
            j = 3
            return 0
        if k <= 0 and answer != 'yes':
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.")
            print(f"Let's try again, {arg}!")
            j = 3
            return 0 
    return 1
