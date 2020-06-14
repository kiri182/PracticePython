import random


def list_comprehension():
    num_list = [i ** 2 for i in range(1, 10, 1)]

    """
  even_list = []
  for j in num_list:
      if j % 2 == 0:
          even_list.append(j)

  print(even_list)
  """

    even_list = [j for j in num_list if j % 2 == 0]
    print(even_list)


list_comprehension()
