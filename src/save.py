import os

def save(information: []):
    with open("game_data.txt", "r+") as file:
        everything = file.read() + information
        file.write(everything + "\n")

def load():
    with open("game_data.txt", "r") as file:
        pass
