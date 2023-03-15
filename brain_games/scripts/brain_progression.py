#!/usr/bin/env python3
from ..cli import welcome_user
from ..cli import goodbye
from ..games.calc_fun import ch_in_prog


def main():
    print('Welcome to the Brain Games!')
    n = welcome_user()
    if ch_in_prog(n) == 1:
        goodbye(n)


if __name__ == '__main__':
    main()
