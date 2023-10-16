#!/usr/bin/python3

""" Minimum Operations """


def minOperations(n: int) -> int:
    """
    Calculates the fewest number of operations needed to
    result in exactly n H characters in the file.
    """
    if not isinstance(n, int):
        return 0

    operations = 0
    iterator = 2
    while (iterator <= n):
        print("{} % {} is {}".format(n, iterator, n % iterator))
        if not (n % iterator):
            print("Get in here")
            n = int(n / iterator)
            operations += iterator
            iterator = 1
        iterator += 1
    return operations
