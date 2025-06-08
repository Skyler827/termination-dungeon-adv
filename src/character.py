import random

global player_health, player_damage
player_health, player_damage = 0, 0

def player_damage(damage: int) -> int:
    player_health -= damage
    return player_health

def player_dodge(damage: int) -> int: # 25% Dodge Chance
    if (random.randint(1, 4) == 1):
        player_health -= damage
    return player_health

def player_health_potion(potion_amount: int, potion_health: int):
    potion_amount -=1
    player_health += potion_health
    return potion_amount, player_health
