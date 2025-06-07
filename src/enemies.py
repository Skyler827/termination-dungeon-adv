# All definitions of enemies

class general_enemy:
    def __init__(self, name, number, x_position, y_position, health, damage):
        self.name = name
        self.number = number # If there are multiple enemies

        self.x_position = x_position
        self.y_position = y_position

        self.health = health
        self.damage = health
    def __str__(self):
        return f"Identification {self.name}, Number {self.number}, Location: X {self.x_position} Y {self.y_position}, Health {self.health}, Damage {self.damage}"
