import random


def create_list():
    check_list = []
    for i in range(10):
        check_list.append(random.randint(1, 10))
    return check_list


def check_num(x):
    result_list = []
    for i in x:
        if i <= 5:
            result_list.append(i)
    print(result_list)


check_num(create_list())
