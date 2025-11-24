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

    print('Welcome to the Trivia Game: Battle of the Worlds. You will enjoy answering questions relating to different topics depending on the world you stumble upon. There are only four rules for the game: choose an intelligence value between 1 and 10, you have 3 lives, all answers must start with a capital letter, and no punctuation when answering questions.')
    name = input('name: ')
    intelligence = input('intelligence: ')
    wisdom = input('wisdom: ')

    player = Player(name, int(intelligence), int(wisdom))

    print('Your name is ' + player.name + '.')

    world = ''
    input('Press Enter to roll a d6.')
    roll = player.roll_d6()
    if roll == 1 or roll == 2:
        print('Hello, fine player! Fate has decided that you will venture into the Demiworld, a world of darkness and danger ruled by the great Demagorgan!')
        world = 'DemiWorld'
    elif roll == 3 or roll == 4: 
        print('Hello, fine player! Fate has decided that you will venture into the Fairyworld, a land of nature and magic ruled by the benevolent Fairy Princess!')
        world = 'Fairyworld'
    elif roll == 5 or roll == 6:
        print('Hello, fine player! Fate has decided that you will venture into Burningdom, a world of constant fire and magma ruled by the Lord of the Flames!') 
        world = 'Buringdom'
    
        if world == 'Buringdom':
            q1 = input('What is the first letter of the alphabet?\n')
            if q1 != 'A':
                print('ERr wrong answer')
            player.lives -= 1
        else:
            print('Great job!')
        q2 = input('Which planet is the only known planet where fire can burn?\n')
        if q2 != 'Earth':
            print('ERr wrong answer')
            player.lives -= 1
        else:
            print('Great job!')
        q3 = input('What happens to cotton if you apply super glue to it?\n')
        if q3 != 'It will catch on fire':
            print('ERr wrong answer')
            player.lives -= 1
        else:
            print('Great job!')
        q4 = input('What are the three elements of the fire triangle?\n')
        if q4 != 'Fuel, oxygen, and heat':
            print('ERr wrong answer')
            player.lives -= 1
        else:
            print('Great job!')
        q5 = input('What should you do if your clothes catch fire?\n')
        if q5 != 'Stop, drop, and roll':
            print('ERr wrong answer')
            player.lives -= 1
        else:
            print('Great job!')
        q6 = input('What are the fire extinguishing mechanisms\n')
        if q6 != 'Starving, smothering, cooling':
            print('ERr wrong answer')
            player.lives -= 1
        else:
            print('Great job!')
        print('Thank you for playing! I hope you survived Buringdom.')
    
    if world == 'Fairyworld':
        q1 = input('An anoxic environment wouldn’t be great for humans, but certain organisms thrive in them. Anoxic means that which element needed by most life to survive is absent?\n')
        if q1 != 'Oxygen':
            print('ERr wrong answer')
            player.lives -= 1
        else:
            print("great job!")
        q2 = input("Which color certificate is a tradable commodity that can be “earned” for generating renewable energy?\n")
        if q2 != 'Green':
            print('ERr wrong answer')
            player.lives -= 1
        else:
            print("great job!")
        q3 = input('What Swedish environmentalist said, "You are never too small to make a difference," in her 2019 speech "Climate Justice Now" at an international conference in Poland?\n')
        if q3 != 'Greta Thunberg':
            print('ERr wrong answer')
            player.lives -= 1
        else:
            print('Great job!')
        q4 = input('A major potential in efforts to engineer environmental sustainability is attempts to breed bacteria that can eat what polymer-based materials that are difficult to recycle?\n')
        if q4 != 'Plastic':
            print('ERr wrong answer')
            player.lives -= 1
        else:
            print('Great job!')
        q5 = input('The largest living species of tortoise in the world is native to what island archipelago in the Pacific Ocean?\n')
        if q5 != 'Galapagos':
            print('ERr wrong answer')
            player.lives -= 1
        else:
            print('Great job!')
        q6 = input('What is the three-letter acronym of the international organization established in 1961 whose purpose is environmentalism and conservation?\n')
        if q6 != 'WWF':
            print('ERr wrong answer')
            player.lives -= 1
        else:
            print('Great job!')
        print('Thank you for playing! I hope you survived Fairyworld.')
    

    if world == 'Demiworld':
        q1 = input('What monster transforms into its monster form during the full moon?\n')
        if q1 != 'Pegasus':
            print('ERr wrong answer')
            player.lives -= 1
        else:
            print("great job!")
        q2 = input('Another white horse, but instead of wings it has a single horn growing from its forehead.\n')
        if q2 != 'Unicorn':
            print('ERr wrong answer')
            player.lives -= 1
        else:
            print('Great job!')
        q3 = input('This fearsome creature had the body of a man, but the head of a bull.\n')
        if q3 != 'Minotaur':
            print('ERr wrong answer')
            player.lives -= 1
        else:
            print('Great job!')
        q4 = input('One of the most popular mythical creatures, this term refers to a giant lizard-like creature, which often breathes fire.\n')
        if q4 != 'Dragon':
            print('ERr wrong answer')
            player.lives -= 1
        else:
            print('Great job!')
        q5 = input('It is the living dead, a man (or woman) who feasts on the blood of the living. It roams the night in search of prey, but is destroyed by sunlight.\n')
        if q5 != 'Vampire':
            print('ERr wrong answer')
            player.lives -= 1
        else:
            print('Great job!')
        q6 = input('This is a three-headed dog who guards the gates of Hades.\n')
        if q6 != 'Cerburus':
            print('ERr wrong answer')
            player.lives -= 1
        else:
            print('Great job!')
        print('Thank you for playing! I hope you survived Demiworld.')
        
    # r = random.randint(0,2)
    # answer = input(questions[r] + '')
    # if answer() == answers[r]:
        # print('correct')
    # else:
        # print('inccorrect')

        
    

    
