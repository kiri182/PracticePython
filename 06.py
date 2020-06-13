

def palindrome():
    try:
        input_str = input('Type a string you like: ')
        list(input_str)
        n = 0
        m = 1
        for i in range(len(input_str)):
            if input_str[n] == input_str[-m]:
                n = n + 1
                m = m + 1
                if n >= len(input_str):
                    print('Confirmed that the string you type was a "palindrome".')
                    break

            else:
                print('Okay, that was not a "palindrome" I want to have...')
                break
    except:
        print('Invalid error.')


palindrome()
