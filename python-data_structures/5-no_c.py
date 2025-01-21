#!/usr/bin/python3
def no_c(my_string):
    """
    Supprime toutes les occurrences
    des caractères 'c' et 'C' d'une chaîne de caractères.

    Args:
        my_string (str): La chaîne de caractères à traiter.

    Returns:
        str: Une nouvelle chaîne de caractères sans les 'c' et 'C'.
    """
    # Initialise une nouvelle chaîne vide pour stocker le résultat
    new_string = ""

    # Parcourt chaque caractère de la chaîne d'entrée
    for char in my_string:
        # Ajoute le caractère à la nouvelle chaîne s'il n'est pas 'c' ou 'C'
        if char != 'c' and char != 'C':
            new_string += char

    # Retourne la nouvelle chaîne de caractères sans 'c' ou 'C'
    return new_string
