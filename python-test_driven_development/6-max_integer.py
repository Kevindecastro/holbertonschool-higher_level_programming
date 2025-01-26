#!/usr/bin/python3
"""Module pour trouver l'entier maximum dans une liste
"""


def max_integer(list=[]):
    """ Fonction pour trouver et retourner le plus grand entier
        dans une liste d'entiers Si la liste est vide,
        la fonction retourne None
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
