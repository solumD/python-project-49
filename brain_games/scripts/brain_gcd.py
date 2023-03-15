#!/usr/bin/env python3
from ..cli import welcome_user
from ..cli import goodbye
from ..games.calc_fun import greatest_divisor


def main():
    print('Welcome to the Brain Games!')
    n = welcome_user()
    if greatest_divisor(n) == 1:
        goodbye(n)


if __name__ == '__main__':
    main()
