#!/usr/bin/python3

def element_at(my_list, idx):
    """
    Récupère un élément d'une liste à un index spécifié.

    Args:
        my_list (list): La liste dont on veut récupérer un élément.
        idx (int): L'index de l'élément à récupérer.

    Returns:
        L'élément à l'index spécifié si l'index est valide.
        Retourne None si l'index est invalide.
    """
    # Vérifie si l'index est en dehors des limites de la liste
    if idx < 0 or idx >= len(my_list):
        # Retourne None si l'index est invalide
        return None

    # Retourne l'élément à l'index spécifié
    return my_list[idx]
