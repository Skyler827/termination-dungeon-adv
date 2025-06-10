import os

def play_sound(file):
    os.system("mpg123 " + file + " &>/dev/null")
