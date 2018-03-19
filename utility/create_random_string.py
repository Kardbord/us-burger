import random
import string


def create_random_string(digit_weight=20, string_length=5):
    random_string = ''

    for x in range(string_length):
        random_int = random.randint(1, 100)

        if random_int <= digit_weight:
            random_string += str(random.randint(1, 9))
        else:
            random_string += random.choice(string.ascii_letters)

    return random_string
