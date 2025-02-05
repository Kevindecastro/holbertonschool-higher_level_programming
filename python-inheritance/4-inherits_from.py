#!/usr/bin/python3
"""
Module contenant la fonction inherits_from

Cette fonction permet de vérifier si un objet est une instance d'une classe
qui hérite (directement ou indirectement) de la classe spécifiée
"""


def inherits_from(obj, a_class):
    """
    Retourne True si l'objet est une instance d'une classe qui hérite de
    a_class (directement ou indirectement), sinon retourne False

    Args:
        obj (object): L'objet à vérifier
        a_class (type): La classe à comparer

    Returns:
        bool: True si obj hérite de a_class, False sinon
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
