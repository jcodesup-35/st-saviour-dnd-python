class Player:
    def_init_(self, name: str, role: str, strength: int, intelligence: int, weakness: int):
    self.name = name
    self.role = role
    self.strength = 50
    self.intelligence = 50
    self.weakness = 50

    def roll














player_1 = Player('')
option = input('Press A to roll advantage or Enter to roll a d20')
if option.lower == 'a':
    player_1.roll_advantage()
else:
    player_1.roll_d20()