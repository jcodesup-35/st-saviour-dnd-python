import random
import time

from player import Player
from draw import draw_d20, draw_d6, draw_d4

def print_dramatic_text(text: str, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

if __name__ == '__main__':
    # create character by collecting user input (name + class)
    # print character sheet
    # specify roll that must be beat and enemy initiative by collecting user input
    # any buffs / debuffs?
    # any critical success / failure?

    name = input('name: ')
    strength = input('strength: ')
    intelligence = input('intelligence: ')
    weakness = input('weakness: ')

    player = Player(name, int(strength), int(intelligence), weakness)

    print('Your name is ' + player.name + '.')

    world = ''
    input('Press Enter to roll a d6.')
    roll = player.roll_d6()
    if roll == 1 or roll == 2:
        print('Hello, fine player! Fate has decided that you will venture into the DemiWorld, a world of darkness and danger ruled by the great Demagorgan!')
        world = 'DemiWorld'
    elif roll == 3 or roll == 4: 
        print('Hello, fine player! Fate has decided that you will venture into the Fairyworld, a land of nature and magic ruled by the benevolent Fairy Princess!')
        world = 'Fairyworld'
    elif roll == 5 or roll == 6:
        print('Hello, fine player! Fate has decided that you will venture into Burningdom, a world of constant fire and magma ruled by the Lord of the Flames!') 
        world = 'Buringdom'
    

    while Player.lives == 5:
        q1 = input("What's the first letter of the alphabet?\n")
        if q1 != "A":
            print("ERr wrong answer forehed")
            player.lives -= 1
        else:
            print("great job!")
        
        
    

    
