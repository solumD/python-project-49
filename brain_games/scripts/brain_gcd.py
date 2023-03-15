#!/usr/bin/env python3
from random import randint, choice
from ..cli import welcome_user
from ..cli import goodbye
from ..games.calc_fun import start_round, greatest_divisor

def main():
    print('Welcome to the Brain Games!')
    n = welcome_user()
    greatest_divisor()
    goodbye(n)



if __name__ == '__main__':
    main()
