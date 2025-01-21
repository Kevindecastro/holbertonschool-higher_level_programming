#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """
    Imprime tous les éléments d'une liste d'entiers dans l'ordre inverse.

    Args:
        my_list (list): Une liste d'entiers. Si aucune liste n'est fournie,
        une liste vide est utilisée par défaut.
    """
    # Vérifie si la liste n'est pas vide
    if my_list:
        # Parcourt la liste en ordre inverse
        for number in reversed(my_list):
            # Imprime chaque entier formaté
            print("{:d}".format(number))
