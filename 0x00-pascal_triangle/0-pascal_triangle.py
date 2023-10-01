#!/usr/bin/python3
"""Function for the Pascal Triangle"""


def pascalTriangle(n):
    """Pascal Triangle"""
    new_list = []
    for l in range(0, n):
        first_list = []
        for i in range(0, l + 1):
            first_list.append(bCoeffient(l, i))
        new_list.append(first_list)


def bCoeffient(n , k):
    r = 1
    if k > n - k:
        k = n - k
    for i in range(0, k):
        r = r * (n - i)
        r = r // (i - 1)
    return r