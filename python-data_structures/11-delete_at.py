#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """
    Supprime un élément d'une liste à un index spécifié.

    Args:
        my_list (list): La liste dont un élément doit être supprimé.
        idx (int): L'index de l'élément à supprimer.
                   Par défaut, l'index est 0.

    Returns:
        list: La liste modifiée avec l'élément supprimé
              si l'index est valide.
              Retourne la liste originale si l'index est invalide.
    """
    # Vérifie si l'index est en dehors des limites de la liste
    if idx < 0 or idx >= len(my_list):
        # Retourne la liste originale si l'index est invalide
        return my_list

    # Supprime l'élément à l'index spécifié
    del my_list[idx]

    # Retourne la liste modifiée
    return my_list
