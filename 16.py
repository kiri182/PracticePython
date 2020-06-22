import random
import string


def create_password():
    print("Let's create your new password.")
    try:
        i = input(
            'Kindly type how many digit do you want to have for the password ?: ')

        source = string.ascii_letters + string.digits + string.punctuation
        password = random.choices(source, k=int(i))
        print("Your new password is: " + ''.join(password))
    except:
        print('Invalid error. Retry again, please.')


create_password()
