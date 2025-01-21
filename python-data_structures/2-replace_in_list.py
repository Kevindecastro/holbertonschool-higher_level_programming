#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """
    Remplace un élément dans une liste à un index spécifié.

    Args:
        my_list (list): La liste dans laquelle l'élément doit être remplacé.
        idx (int): L'index de l'élément à remplacer.
        element: Le nouvel élément à insérer à l'index spécifié.

    Returns:
        list: La liste avec l'élément remplacé si l'index est valide.
              Sinon, retourne la liste originale inchangée.
    """
    # Vérifie si l'index est en dehors des limites de la liste
    if idx < 0 or idx >= len(my_list):
        # Retourne la liste originale si l'index est invalide
        return my_list

    # Remplace l'élément à l'index spécifié par le nouvel élément
    my_list[idx] = element

    # Retourne la liste modifiée
    return my_list
