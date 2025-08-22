import os

MAX_FILE_LENGTH = 1000

def save(information: []):
    with open("save-data/game_data.txt", "r+") as file:
        if len(file.readlines()) > MAX_FILE_LENGTH:
            die("Game data includes unreasonable amount of data exceeding max length")
        everything = file.read() + information + '\n'
        file.write(everything)

def load():
    try:
        with open("save-data/game_data.txt", "r") as file:
            pass
    except Exception as e:
        die(e)
