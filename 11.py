def check_divisors():
    div_list = [1]
    try:
        num = input('Number?: ')

        for i in range(2, int(num)+1, 1):
            if int(num) % i == 0:
                div_list.append(i)
        print(div_list)
        print('These are divisors of what you typed.')
        a = len(div_list)
        return a
    except ValueError:
        print('Invalid error. Please type an integer.')


def check_prime(x):
    if x == 2:
        print('So, the number you typed is prime.')
    else:
        print('So, the number you typed is NOT prime.')


check_prime(check_divisors())
