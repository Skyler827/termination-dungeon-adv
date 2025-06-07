# Two dimensional board

import os

columns, width = os.get_terminal_size(0)
if columns or width <= 15:
    print("Width is too small")
    exit()
