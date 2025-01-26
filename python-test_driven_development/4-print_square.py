#!/usr/bin/python3
"""
Imprime un carré de taille spécifiée avec le caractère '#'.
"""


def print_square(size):
    """
    Imprime un carré de taille 'size' avec le caractère '#',
    ou soulève une exception si 'size' est invalide.

    Args:
        size (int): La taille du carré à imprimer.

    Raises:
        TypeError: Si 'size' n'est pas un entier ou si 'size' est un float < 0.
        ValueError: Si 'size' est un entier < 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
