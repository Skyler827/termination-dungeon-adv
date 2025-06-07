from blessed import Terminal
import re
import math
from colorama import Fore, Back, Style
from functools import reduce
import blessed

from colors import *
import board
import enemies

def main():
    print(RED + "Hello world")
    board.board_check_size()
    my_enemy = enemies.general_enemy("slime", 1, 5, 5, 100, 25)
    print(my_enemy)

    run = True
    while run:
        pass

if __name__ == "__main__":
    main()
