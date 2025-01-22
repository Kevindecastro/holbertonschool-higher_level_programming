#!/usr/bin/python3

def max_integer(my_list=[]):
    """
    Retourne la valeur maximale dans une liste d'entiers.
    Si la liste est vide, retourne None.

    Args:
        my_list (list): Une liste d'entiers.
        Si aucune liste n'est fournie,
        une liste vide est utilisée par défaut.

    Returns:
        int or None: La valeur maximale dans la liste,
        ou None si la liste est vide.
    """
    # Vérifie si la liste est vide
    if not my_list:
        # Retourne None si la liste est vide
        return None

    # Initialise max_val avec le premier élément de la liste
    max_val = my_list[0]

    # Parcourt chaque élément de la liste
    for number in my_list:
        # Met à jour max_val si un élément plus grand est trouvé
        if number > max_val:
            max_val = number

    # Retourne la valeur maximale trouvée
    return max_val
