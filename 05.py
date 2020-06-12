import random


def listscommon():
    list_i = []
    list_j = []
    result = []

    for i in [random.randint(1, 10) for x in range(10)]:
        list_i.append(i)
    for j in [random.randint(1, 10) for x in range(10)]:
        list_j.append(j)

    for i in list_i:
        if i in list_j:
            if i not in result:
                result.append(i)

    print('1st list is as below:')
    print(list_i)
    print('Then 2nd list is as below:')
    print(list_j)
    print('Thus common numbers are as below:')
    print(result)


listscommon()
