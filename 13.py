"""
a1 = a2 = 1
a(n+2) = a(n+1) + an
"""


def createFibonnaci(x):
    num_list = []
    if x <= 2:
        for i in range(x):
            num_list.append(1)
    else:
        for i in range(x):
            if i < 2:
                num_list.append(1)
            else:
                num_list.append(num_list[i-2] + num_list[i-1])

    print(num_list)


try:
    user_inpout = input('How many?: ')
    createFibonnaci(int(user_inpout))
except:
    print('Invalid error. Please type a number.')
