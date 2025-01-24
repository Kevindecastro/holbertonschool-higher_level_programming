#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    Imprime les x premiers éléments d'une liste en toute sécurité.

    Args:
        my_list (list): Liste à parcourir.
        x (int): Nombre d'éléments à imprimer.

    Returns:
        int: Nombre d'éléments effectivement imprimés.
    """
    count = 0
    try:
        for i in range(x):  # Parcours jusqu'à x éléments
            print(my_list[i], end="")  # Affiche sans saut de ligne
            count += 1
    except IndexError:
        pass  # Ignore si x dépasse la longueur
    print()  # Ajoute un saut de ligne final
    return count
