from math import sqrt

def is_prime(x):

    if x <= 1:
        return False

    for i in range(2, int(round(sqrt(x)) + 1)):
        if x % i == 0:
            return False

    return True
