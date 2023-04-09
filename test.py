def prime_generator(number: int) -> list:
    """
    This function returns prime numbers
    :param number: int
    :return: list
    """
    for x in list(range(2, number + 1)):
        if 0 not in [x % k for k in range(2, x)]:
            yield x


print(list(prime_generator(10)))
