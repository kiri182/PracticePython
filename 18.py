import random

Answer = str(random.randrange(0, 10000))
Cows = 0
Bulls = 4
AnswerLine = list(Answer)
# print(AnswerLine)

try:
    print('Welcome to the Cows and Bulls Game!')

    while Cows != 4:
        Cows = 0
        Bulls = 4
        UserInput = input('Enter a number: ')
        UserLine = list(UserInput)
        for i in range(4):
            if UserLine[i] == AnswerLine[i]:
                Cows += 1

        Bulls = Bulls - Cows
        print(str(Cows) + ' cows, ' + str(Bulls) + 'bulls.')

        continue

except:
    print('Invalid error. Enter 4 digit number.')
