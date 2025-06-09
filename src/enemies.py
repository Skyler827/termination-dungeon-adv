# All definitions of enemies

class general_enemy:
    def __init__(self, name, number, x_position, y_position, health, damage):
        self.name = name
        self.number = number # If there are multiple enemies

        self.x_position = x_position
        self.y_position = y_position

        self.health = health
        self.damage = health

    def hit(self, damage):
        self.health -= damage
        if (self.health <= 0):
            del self

    def __str__(self):
        return f"General Enemy {self.name}, Number {self.number}, Location: X {self.x_position} Y {self.y_position}, Health {self.health}, Damage {self.damage}"

class boss:
    def __init__(self, name, stage, x_position, y_position, health, original_health, damage):
        self.name = name
        self.stage = stage

        self.x_position = x_position
        self.y_position = y_position

        self.health = health
        self.original_health = original_health # This value doesn't change
        self.damage = health
    
    def multiple_boss_stages(self, health, original_health):
        if self.health <= 0 and self.stages > 1:
            self.health += self.original_health

    def hit(self, damage):
        self.health -= damage
        if (self.health <= 0): # TODO Later add above func to this
            del self

    def __str__(self):
        return f"Boss {self.name}, Number {self.number}, Location: X {self.x_position} Y {self.y_position}, Health {self.health}, Damage {self.damage}"

