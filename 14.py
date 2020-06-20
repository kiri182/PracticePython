import random


def setfunction():
    first_list = []
    first_list = [random.randint(1, 5) for i in range(5)]
    converted_list = list(set(first_list))

    print(first_list)
    print(converted_list)


setfunction()
