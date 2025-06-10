import sys
from blessed import Terminal
import re
import math
from colorama import Fore, Back, Style
from functools import reduce
import blessed
import threading

sys.path.insert(0, 'src/')
from colors import *
from character import *
from save import *
from board import *
from enemies import *
from audio import *

def testing(): # DEBUGGING
    #game_over()
    print(RED + "Hello world")
    board_check_size()
    my_enemy = general_enemy("slime", 1, 5, 5, 100, 25)
    
    # Two valid ways of doing damage, player_does_damage includes chance
    #my_enemy.hit(90)
    #my_enemy.health = player_does_damage(my_enemy.health)

    print(my_enemy.health)
    save("TEXT")

def invalid_choice():
    print(RED + "Invalid Choice")

def game_over():
    terminal_clear()
    print(RED +  "Game Over" + RESET + "\n1: Play again\n2: Exit")
    game_choice = input()
    if game_choice == "1": menu()
    elif game_choice == "2": exit()
    else: menu()

def menu():
    terminal_clear()
    t1 = threading.Thread(target=play_sound, args=("~/programs/git/termination-dungeon-adv/assets/audio/main_menu.mp3",))
    t1.start()
    print(BLUE + "Welcome to Termination Dungeon Adventure" + RESET + "\n1: Play\n2: Exit")
    player_choice = input()
    
    if player_choice == "1": testing()
    elif player_choice == "2": exit()
    else: invalid_choice()
    terminal_clear()

def main():
    run = True
    while run:
        menu()

if __name__ == "__main__":
    main()
