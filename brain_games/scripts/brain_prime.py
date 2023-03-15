#!/usr/bin/env python3
from random import randint, choice
from ..cli import welcome_user
from ..cli import goodbye
from ..games.calc_fun import ch_prime

def main():
    print('Welcome to the Brain Games!')
    n = welcome_user()
    ch_prime()
    goodbye(n)