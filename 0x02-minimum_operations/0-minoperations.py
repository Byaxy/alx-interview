#!/usr/bin/python3
""" Minimum Operations """


def minOperations(n):
    """ Return: total """
    x, y = 0, 2
    while n > 1:
        while not n % y:
            x += y
            n /= y
        y += 1
    return x