#!/usr/bin/python3

def multiply_list_map(my_list=None, number=0):
    """
    Multiplie chaque élément de la liste par 'number' et retourne une nouvelle
    liste.

    Args:
        my_list (list, optional): Liste des éléments à multiplier. Par défaut,
            c'est une liste vide.
        number (int, float): Le facteur de multiplication.

    Returns:
        list: Une nouvelle liste où chaque élément est multiplié par 'number'.
    """

    # Si aucune liste n'est fournie,
    # on initialise 'my_list' comme une liste vide.
    if my_list is None:
        my_list = []

    # Utilisation d'une compréhension de liste pour multiplier chaque élément
    # par 'number'. Cela crée une nouvelle liste avec les résultats.
    return [x * number for x in my_list]
