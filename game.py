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

    # introduces rules using a string that is printed to users
    print('Welcome to the Trivia Game: Battle of the Worlds. You will enjoy ' +
    'answering questions relating to different topics depending on the world you stumble ' +
    'upon. There are five rules for the game: choose an intelligence value between 1 ' +
    'and 10, ' + 'choose a wisdom value between 1 and 10' +
    'you have 3 lives, all answers must start with a capital letter, and no ' +
    'punctuation in answers. This is a game of specificity, so be specific.')

    # introduces the game and pulls instances from Player class to accept user input
    # instances are name, intelligence, and wisdom
    # input is the function used to call for user input
    name = input('name: ')
    intelligence = input('Rate your level of intelligence: ')
    wisdom = input('Rate the level of wisdom you possess: ')

    player = Player(name, int(intelligence), int(wisdom))

    print('Your name is ' + player.name + '.')

    # decides the world the player will go to using random numebers
    # imports random function which allows dice roll to work
    # pulls roll_6 function from player.py
    
    world = ''
    input('Press Enter to roll a d6.')
    roll = player.roll_d6()
    if roll == 1 or roll == 2:
        print('Hello, fine player! Fate has decided that you will venture into the ' +
            'Demiworld, a world of darkness and danger ruled by the great Demagorgan!')
        world = 'Demiworld'
    elif roll == 3 or roll == 4: 
        print('Hello, fine player! Fate has decided that you will venture into the ' +
              'Fairyworld, a land of nature and magic ruled by the benevolent Fairy' +
              'Princess!')
        world = 'Fairyworld'
    elif roll == 5 or roll == 6:
        print('Hello, fine player! Fate has decided that you will venture into ' +
              'Burningdom, a world of constant fire and magma ruled by the Lord ' + 
              'of the Flames!')
        world = 'Burningdom'
    
    # indentations, conditions, and if statements hold true for all worlds
    # the question and answer content inside of each world is different
    # a player is directed to the Buringdom through if statements and random numbers
    # once in Burningdom if statement, a player is asked 6 environmental trivia questions
    # indentations are important to expressing the if statements and creating conditions 
    # surrounding lives for the player
    # Player.lives is used to represent the total number of lives and connect it back 
    # to the player class
    
    if world == 'Burningdom':
        if Player.lives > 0:
            q1 = input('What is the first letter of the alphabet?\n')
            if q1 != 'A':
                Player.lives -= 1
                print('ERr wrong answer')
            else:
                print('Great job!')
            q2 = input('Which planet is the only known planet where fire can burn?\n')
            if q2 != 'Earth':
                Player.lives -= 1
                print('ERr wrong answer')
            else:
                print('Great job!')
            q3 = input('What happens to cotton if you apply super glue to it?\n')
            if q3 != 'It will catch on fire':
                Player.lives -= 1
                print('ERr wrong answer')
            else:
                print('Great job!')
            if Player.lives == 0:
                print('GAME OVER!')
            else: 
                q4 = input('What are the three elements of the fire triangle?\n')
                if q4 != 'Fuel, oxygen, and heat':
                    Player.lives -= 1
                    print('ERr wrong answer')
                else:
                    print('Great job!')
                if Player.lives == 0:
                    print('GAME OVER!')
                else:
                    q5 = input('What should you do if your clothes catch fire?\n')
                    if q5 != 'Stop, drop, and roll':
                        Player.lives -= 1
                        print('ERr wrong answer')
                    else:
                        print('Great job!')
                    if Player.lives == 0:
                        print('GAME OVER!')
                    else:
                        q6 = input('What are the fire extinguishing mechanisms?\n')
                        if q6 != 'Starving, smothering, cooling':
                            Player.lives -= 1
                            print('ERr wrong answer')
                        else:
                            print('Great job!')
                        if Player.lives == 0:
                            print('GAME OVER!')
                        else: 
                            print('Thank you for playing! I hope you survived Buringdom. '
                                  + 'If your wisdom and ' + 'intelligence were above 6, you' 
                                  + ' should have survived.')
    
    # a player is directed to the Demiworld through if statements and random numbers
    # once in Demiworld if statement, a player is asked 6 monster/mythology trivia questions
    if world == 'Demiworld':
        q1 = input('What monster transforms into its monster form during the full moon?\n')
        if q1 != 'Pegasus':
            Player.lives -= 1
            print('ERr wrong answer')
        else:
            print("Great job!")
        q2 = input('Another white horse, but instead of wings it has a single horn ' + 
                   'growing from its forehead.\n')
        if q2 != 'Unicorn':
            Player.lives -= 1
            print('ERr wrong answer')
        else:
            print('Great job!')
        q3 = input('This fearsome creature had the body of a man, but the ' + 
                   'head of a bull.\n')
        if q3 != 'Minotaur':
            Player.lives -= 1
            print('ERr wrong answer')
        else:
            print('Great job!')
        if Player.lives == 0:
            print('GAME OVER!')
        else: 
            q4 = input('One of the most popular mythical creatures, this term refers to a' 
                       + ' giant lizard-like creature, which often breathes fire.\n')
            if q4 != 'Dragon':
                Player.lives -= 1
                print('ERr wrong answer')
            else:
                print('Great job!')
            if Player.lives == 0:
                print('GAME OVER!')
            else: 
                q5 = input('It is the living dead, a man (or woman) who feasts on the blood' 
                           + ' of the living. It roams the night in search of prey, but is ' 
                           + ' destroyed by sunlight.\n')
                if q5 != 'Vampire':
                    Player.lives -= 1
                    print('ERr wrong answer')
                else:
                    print('Great job!')
                if Player.lives == 0:
                    print('GAME OVER!')
                else: 
                    q6 = input('This is a three-headed dog who guards the gates of Hades.\n')
                    if q6 != 'Cerburus':
                        Player.lives -= 1
                        print('ERr wrong answer')
                    else:
                        print('Great job!')
                    if Player.lives == 0:
                        print('GAME OVER!')
                    else:
                        print('Thank you for playing! I hope you survived Demiworld. If '
                              'your wisdom and ' + 'intelligence were above 5, you should '
                              + 'have survived.')

    # a player is directed to the Fairyworld through if statements and random numbers
    # once in Fairyworld if statement, a player is asked 6 environmental trivia questions
    if world == 'Fairyworld':
        q1 = input('An anoxic environment wouldn’t be great for humans, but certain ' + 
                   'organisms thrive in them. Anoxic means that which element needed by ' + 
                   'most life to survive is absent?\n')
        if q1 != 'Oxygen':
            Player.lives -= 1
            print('ERr wrong answer')
        else:
            print("Great job!")
        q2 = input('Which color certificate is a tradable commodity that can be “earned” ' + 
                   'for generating renewable energy?\n')
        if q2 != 'Green':
            Player.lives -= 1
            print('ERr wrong answer')
        else:
            print("Great job!")
        q3 = input('What Swedish environmentalist said, "You are never too small to make ' +
                   'a difference," in her 2019 speech "Climate Justice Now" at an ' +
                   'international' + ' conference in Poland?\n')
        if q3 != 'Greta Thunberg':
            Player.lives -= 1
            print('ERr wrong answer')
        else:
            print('Great job!')
        if Player.lives == 0:
            print('GAME OVER!')
        else: 
            q4 = input('A major potential in efforts to engineer environmental ' +
                       'sustainability is attempts to breed bacteria that can eat what ' +
                       'polymer-based materials that are difficult to recycle?\n')
            if q4 != 'Plastic':
                Player.lives -= 1
                print('ERr wrong answer')
            else:
                print('Great job!')
            if Player.lives == 0:
                print('GAME OVER!')
            else:
                q5 = input('The largest living species of tortoise in the world is native ' +
                           'to what island archipelago in the Pacific Ocean?\n')
                if q5 != 'Galapagos':
                    print('ERr wrong answer')
                else:
                    print('Great job!')
                if Player.lives == 0:
                    print('GAME OVER!')
                else: 
                    q6 = input('What is the three-letter acronym of the international ' +
                               'organization established in 1961 whose purpose is ' +
                               'environmentalism and conservation?\n')
                    if q6 != 'WWF':
                        Player.lives -= 1
                        print('ERr wrong answer')
                    else:
                        print('Great job!')
                    if Player.lives == 0:
                        print('GAME OVER!')
                    else:
                        print('Thank you for playing! I hope you survived Fairyworld. If ' +
                              'your wisdom and intelligence were above 7, you should have '
                              + 'survived.')
    
        
    # way to randomize questions and give constant output depending on input given
    # r = random.randint(0,2)
    # answer = input(questions[r] + '')
    # if answer() == answers[r]:
        # print('correct')
    # else:
        # print('incorrect')

        
    

    
