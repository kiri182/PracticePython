import random


def firstend_return(x, y):
    first_list = []
    for i in [random.randint(1, x) for j in range(y)]:
        first_list.append(i)
    print(first_list)
    print(first_list[0])
    print(first_list[-1])


firstend_return(100, 5)
