#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
    Affiche les x premiers éléments de my_list qui sont des entiers.
    """
    count = 0
    for i in range(x):
        try:
            # Tente d'afficher l'élément comme un entier
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            # Ignore les éléments qui ne sont pas des entiers
            pass
    print("")  # Affiche une nouvelle ligne à la fin
    return count
