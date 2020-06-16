import random

"""
return_list = []
for i in a:
    if i in b:
        if i not in return_list:
            return_list.append(i)
        else:
            continue

print(return_list)
"""

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

a = random.sample(range(1, 30), 12)
b = random.sample(range(1, 30), 16)


x = [i for i in set(a) if i in b]
print(x)
