#!/usr/bin/python3
"""
Module for pascal_triangle method.
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers
    """
    rows = [[1 for c in range(b + 1)] for b in range(n)]
    for n in range(n):
        for b in range(n - 1):
            rows[n][b + 1] = sum(rows[n - 1][b:b + 2])
    return rows
