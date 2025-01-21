#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """
    Crée une nouvelle liste où l'élément à l'index donné
    est remplacé par un nouvel élément.
    Si l'index est invalide, retourne une copie de la liste originale.

    Args:
        my_list (list): La liste d'origine.
        idx (int): L'index de l'élément à remplacer.
        element: Le nouvel élément à insérer à l'index spécifié.

    Returns:
        list: Une nouvelle liste avec l'élément modifié ou
        une copie de la liste originale si l'index est invalide.
    """
    # Vérifie si l'index est en dehors des limites de la liste
    if idx < 0 or idx >= len(my_list):
        # Retourne une copie de la liste originale si l'index est invalide
        return my_list[:]

    # Crée une nouvelle liste en copiant la liste originale
    new_list = my_list[:]

    # Remplace l'élément à l'index spécifié par le nouvel élément
    new_list[idx] = element

    # Retourne la nouvelle liste avec l'élément modifié
    return new_list
