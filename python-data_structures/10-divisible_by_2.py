#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """
    Vérifie quels éléments d'une liste sont divisibles par 2.

    Args:
        my_list (list): Une liste d'entiers.
        Si aucune liste n'est fournie,
        une liste vide est utilisée par défaut.

    Returns:
        list: Une liste de booléens
        où chaque élément est True
        si l'élément correspondant de my_list est divisible par 2,
        sinon False.
    """
    # Utilise une compréhension de liste pour créer une liste de booléens
    # Chaque élément est True si le nombre est divisible par 2
    # (reste de la division par 2 est 0), sinon False
    return [number % 2 == 0 for number in my_list]
