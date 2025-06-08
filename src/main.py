from blessed import Terminal
import re
import math
from colorama import Fore, Back, Style
from functools import reduce
import blessed

from colors import *
from character import *
import save
import board
import enemies

def testing(): # DEBUGGING
    print(RED + "Hello world")
    board.board_check_size()
    my_enemy = enemies.general_enemy("slime", 1, 5, 5, 100, 25)
    my_enemy.hit(90)
    print(my_enemy)
    save.save("TEXT")

def invalid_choice():
    print(RED + "Invalid Choice")

def menu():
    print(BLUE + "Welcome to Termination Dungeon Adventure" + Style.RESET_ALL + "\n1: Play\n2: Exit")
    player_choice = input()
    
    if (player_choice == "1"):
        testing()
    elif (player_choice == "2"):
        exit()
    else:
        invalid_choice()

def main():
    run = True
    while run:
        menu()

if __name__ == "__main__":
    main()
