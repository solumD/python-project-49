#!/usr/bin/python3
import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name

def goodbye(arg):
    return print(f'Congratulations, {arg}!')
