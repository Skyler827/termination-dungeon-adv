# Two dimensional board

import os

global columns, width
columns, width = os.get_terminal_size()

def board_check_size():
    print ("Column size", columns)
    print ("Width size", columns)

    if columns < 15 or width < 15:
        print("Width is too small")
        exit()
