#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
    Imprime les entiers dans la liste jusqu'à x éléments.

    Args:
        my_list (list): Liste à parcourir.
        x (int): Nombre d'éléments à vérifier.

    Returns:
        int: Nombre d'entiers imprimés.
    """
    count = 0
    try:
        for i in range(x):  # Parcours jusqu'à x éléments
            if isinstance(my_list[i], int):  # Vérifie si c'est un entier
                print("{:d}".format(my_list[i]), end="")  # Affiche l'entier
                count += 1
    except IndexError:
        pass  # Ignore si x dépasse la longueur de la liste
    print()  # Ajoute un saut de ligne après l'impression
    return count
