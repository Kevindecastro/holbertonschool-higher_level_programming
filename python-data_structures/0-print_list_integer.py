#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """
    Imprime tous les éléments d'une liste d'entiers.

    Args:
        my_list (list): Une liste d'entiers. Si aucune liste n'est fournie,
        une liste vide est utilisée par défaut.
    """
    # Parcourt chaque élément de la liste
    for number in my_list:
        # Imprime l'élément actuel formaté en tant qu'entier
        print("{:d}".format(number))
