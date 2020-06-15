import random
import sys


def guess():
    computuer_input = random.randint(1, 9)
    try:
        user_input = input(
            "I have a number.Type your favorite number and guess whether that's lower or higher: ")
        if computuer_input > int(user_input):
            print('Your number is lower than mine.')
            print('Yours is ' + str(user_input) +
                  ', and mine is ' + str(computuer_input) + '.')
        elif computuer_input < int(user_input):
            print('Your number is higher than mine.')
            print('Yours is ' + str(user_input) +
                  ', and mine is ' + str(computuer_input) + '.')
        else:
            print('Wow, exactly right!')

        quit = input('Do you wanna play one more again?(y/n): ')
        if quit == 'n':
            print('Bye')
            sys.exit
        else:
            guess()

    except ValueError:
        print('Invalid error.')


guess()
