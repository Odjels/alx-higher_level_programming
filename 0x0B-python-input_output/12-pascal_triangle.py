#!/usr/bin/python3
"""
pascal_triangle method.
"""


def pascal_triangle(n):
    """
    returns a list of the lists of integers
    """
    row = [[1 for c in range(b + 1)] for b in range(n)]
    for n in range(n):
        for b in range(n - 1):
            row[n][b + 1] = sum(row[n - 1][b:b + 2])
    return row
