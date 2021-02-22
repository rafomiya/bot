from random import randint

def get_random_dimension() -> tuple:
    x = randint(300, 1000)
    y = randint(300, 1000)

    return (x, y)
