#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Utilisation d'une compréhension de liste pour parcourir chaque ligne
    # (row) de la matrice
    return [
        [x ** 2 for x in row]  # Pour chaque élément 'x' dans la ligne,
        # calculer son carré (x^2)
        for row in matrix  # Parcourir chaque ligne de la matrice et appliquer
        # l'opération à chaque élément
    ]
