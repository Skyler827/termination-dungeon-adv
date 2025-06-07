from blessed import Terminal
import re
import math
from colorama import Fore, Back, Style
from functools import reduce
import blessed

from board import board_check_size

def main():
    print("Hello world")
    board_check_size()

if __name__ == "__main__":
    main()
