def wears_jacket_with_if(temp, raining):
    """
    When temp is below 60 degree or raining, returns True.
    >>> wears_jacket_with_if(90, False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(100, True)
    True
    """
    return temp < 60 or raining


def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """
    i = 2
    while i <= (n // 2):
        if n % i == 0:
            return False
        i += 1
    return True


