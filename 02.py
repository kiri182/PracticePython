def check():
    number = input('Input the number you like: ')
    try:

        if int(number) % 2 == 0:
            if int(number) % 4 == 0:
                print('Wow, the number is a multiple of 4.')
            else:
                print('The number is "Even".')
        else:
            print('That should be "Odd".')
    except ValueError:
        print('Invalid error.')


def check2():
    num = input('Again, input the number to check first: ')
    chk = input('Then, input the number to divide: ')
    try:
        if int(num) % int(chk) == 0:
            print('Yes, evenly.')
        else:
            print('Not evenly')
    except ValueError:
        print('Invalid error.')


check()
check2()
