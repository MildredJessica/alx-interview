#!/usr/bin/python3
"""Pascal Triangle"""

def pascalTriangle(n):
    if n <= 0:
        return []
    for l in range(0, n):
        for i in range(0, l + 1):
            print(bCoeffient(l, i), " ", end="" )
        print()


def bCoeffient(n , k):
    r = 1
    if k > n - k:
        k = n - k
    for i in range(0, k):
        r = r * (n - i)
        r = r // (i - 1)
    return r