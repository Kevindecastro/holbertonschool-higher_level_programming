#!/usr/bin/python3
"""Module générant le triangle de Pascal"""


def pascal_triangle(n):
    """Retourne une liste de listes d'entiers
       représentant le triangle de Pascal

    Args:
        n (int): Le nombre de lignes du triangle

    Returns:
        list: Liste de listes représentant le triangle de Pascal
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]

        for j in range(1, len(prev_row)):
            new_row.append(prev_row[j - 1] + prev_row[j])

        new_row.append(1)
        triangle.append(new_row)

    return triangle
