#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """
    Returns a list of integers
    representing the Pascal Triangle of n
    returns empty list if n <= 0
    """
    triangle = []
    if n <= 0:
        return triangle
    triangle = [[1]]
    for row_num in range(1, n):
        row = [1]
        for col in range(len(triangle[row_num - 1]) - 1):
            prev_row = triangle[row_num - 1]
            row.append(prev_row[col] + prev_row[col + 1])
        row.append(1)
        triangle.append(row)
    return triangle
