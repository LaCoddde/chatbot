# Program to clear screen

import os
from subprocess import call
from time import sleep


def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')
