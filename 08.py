"""
Rock beats scissors
Scissors beats paper
Paper beats rock
"""

import random
import sys

game = {'1': 'Rock', "2": 'Scissors', "3": 'Paper'}


def playgame():
    computer_input = random.randint(1, 3)
    player_input = input(
        'Type the number. Rock:1, Scissors:2, Paper:3? : ')
    player = game[player_input]
    computer = game[str(computer_input)]

    if player == computer:
        print('Rock, paper, scissors!')
    elif (player == 'Rock' and computer == 'Scissors') or (player == 'Scissors' and computer == 'Paper') or (player == 'Paper' and computer == 'Rock'):
        print('You win.')
    else:
        print('You lose.')

    quit = input('Do you wanna play one more again?(y/n): ')
    if quit == 'n':
        print('Bye')
        sys.exit
    else:
        playgame()


playgame()
