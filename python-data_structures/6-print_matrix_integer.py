#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """
    Imprime une matrice d'entiers, chaque ligne sur une nouvelle ligne,
    avec les éléments séparés par des espaces.

    Args:
        matrix (list of lists):
        Une liste de listes d'entiers représentant la matrice.
        Si aucune matrice n'est fournie,
        une matrice vide par défaut est utilisée.
    """
    # Parcourt chaque ligne de la matrice
    for row in matrix:
        # Joint les éléments de la ligne en une seule chaîne,
        # séparés par des espaces, et les imprime formatés comme des entiers
        print(" ".join("{:d}".format(element) for element in row))
