import random
from draw import draw_d20, draw_d6

class Player:
    def __init__(self, name: str, wisdom: int, intelligence: int):
        self.name = name
        self.lives = 3
        self.intelligence = intelligence
        self.wisdom = wisdom
        

    def roll_d6(self) -> int:
        roll = random.randint(1, 6)
        draw_d6(roll)
        return roll
    

#class Dog:
    #def __init__(self, name: str, breed: str):
        #self.name = name
        #self.breed = breed
        #self.tail = True
        #self.legs = 4
        #self.ers = 2
    #def bark(self) -> None:
        #print(self.name + 'the ' + self.breed + 'barks ... woof! woof!')

    #first_dog = Dog('Bluey', 'Blue Heeler')
    #first_dog.bark()

    #second_dog = Dog('Lassie', 'Collie')
    #second_dog.bark()

    #def terrible accident(self) -> None: 
