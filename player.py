import random
from draw import draw_d20, draw_d6

class Player:
    def __init__(self, name: str, role: str, strength: int, intelligence: int, weakness: str):
        self.name = name
        self.role = role
        self.strength = strength
        self.intelligence = intelligence
        self.weakness = weakness

    def roll_d6(self) -> int:
        roll = random.randint(1, 6)
        draw_d6(roll)
        return roll
