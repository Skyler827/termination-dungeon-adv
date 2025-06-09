import os

def die(message: str):
    print(message)
    exit(1)

def save(information: []):
    with open("game_data.txt", "r+") as file:
        if len(file.readlines()) > 1000:
            die("Game data includes unreasonable amount of data exceeding max length")
        everything = file.read() + information
        file.write(everything + "\n")

def load():
    try:
        with open("game_data.txt", "r") as file:
            pass
    except Exception as e:
        die(e)
