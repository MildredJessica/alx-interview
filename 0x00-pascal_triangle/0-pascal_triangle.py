#!/usr/bin/python3
"""Function for the Pascal Triangle"""


def pascal_triangle(n):
    """Pascal Triangle"""
    new_list = []
    if n <= 0:
        return new_list
    for l in range( n):
        first_list = []
        for i in range(l + 1):
            first_list.append(factorial(l)//(factorial(i)*factorial(l-i)))
            print(first_list)
        new_list.append(first_list)
    return new_list


def factorial(n):
    """Calculates the factorial"""
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1)