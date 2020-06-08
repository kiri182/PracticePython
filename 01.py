import datetime


def future():
    td = datetime.date.today()
    name = input('May I know your name?: ')
    age = input('How old are you?: ')
    agedif = 100 - int(age)
    if agedif <= 0:
        print('You live a long life...!')
    else:
        future = agedif + td.year
        print('Hi, ' + name + '. You will be 100yo at ' + str(future))


future()
