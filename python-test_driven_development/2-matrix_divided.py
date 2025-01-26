#!/usr/bin/python3
"""
Module 2-matrix_divided
Contains a function that divides all elements of a matrix by a number.
"""


def matrix_divided(matrix, div):
    """
    Divise tous les éléments d'une matrice par un nombre donné,
    et retourne une nouvelle matrice avec les résultats arrondis à 2 décimales.

    Args:
        matrix (list of list of int/float): La matrice à diviser.
        div (int/float): Le diviseur.

    Raises:
        TypeError: Si matrix n'est pas une liste de listes d'entiers
                   ou de flottants.
        TypeError: Si chaque ligne de matrix n'a pas la même taille.
        TypeError: Si div n'est pas un nombre.
        ZeroDivisionError: Si div est égal à 0.

    Returns:
        list of list of float: Une nouvelle matrice avec les résultats
                               de la division.
    """
    invalid_mat = "matrix must be a matrix (list of lists) of integers/floats"

    # Vérifier que matrix est une liste non vide
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(invalid_mat)

    # Vérifier que matrix est une liste de listes et qu'aucune ligne n'est vide
    if not all(isinstance(row, list) for row in matrix) or any(
            len(row) == 0 for row in matrix):
        raise TypeError(invalid_mat)

    # Vérifier que chaque élément est un entier ou un flottant
    if not all(isinstance(element, (int, float))
               for row in matrix for element in row):
        raise TypeError(invalid_mat)

    # Vérifier que toutes les lignes ont la même taille
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Vérifier que div est un nombre
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Vérifier que div n'est pas égal à 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Effectuer la division et arrondir les résultats à 2 décimales
    return [[round(element / div, 2) for element in row] for row in matrix]
