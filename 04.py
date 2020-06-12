

def check_divisors():
    div_list = [1]
    try:
        num = input('Number?: ')

        for i in range(2, int(num)+1, 1):
            if int(num) % i == 0:
                div_list.append(i)
        print(div_list)
        print('These are divisors of what you typed.')
    except ValueError:
        print('Invalid error. Please type an integer.')


check_divisors()
