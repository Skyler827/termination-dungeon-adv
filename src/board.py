import os

import colors

global columns, width, board_tiles, x, y

x, y = 0, 0
board_tiles = [0][0]
columns, width = os.get_terminal_size()

def terminal_clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def board_check_size():
    while True:
        if columns < 15 or width < 15:
            terminal_clear()
            print(RED + "Terminal size is too small")
            time.sleep(1)
        else:
            break
