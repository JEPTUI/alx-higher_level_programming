#!/usr/bin/python3
""" Module - 12-pascal_triangle
Defines a function that returns a list of lists of integers
representing the Pascal’s triangle
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing
    the Pascal’s triangle of n
    """
    if n <= 0:
        return []
    if n == 1:
        return [[1]]

    triangle = [[1]]
    for rows in range(n-1):
        triangle.append([i+j for i, j in zip([0] +
                        triangle[-1], triangle[-1] + [0])])
    return triangle
