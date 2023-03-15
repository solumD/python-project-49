#!/usr/bin/env python3
from random import randint, choice
from ..cli import welcome_user
from ..cli import goodbye
from ..games.calc_fun import start_round

def main():
    print('Welcome to the Brain Games!')
    n = welcome_user()
    if start_round(n) == 1:
        goodbye(n)



if __name__ == '__main__':
    main()
