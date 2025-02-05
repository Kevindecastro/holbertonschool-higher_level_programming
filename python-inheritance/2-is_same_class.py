#!/usr/bin/python3
"""
Module contenant la fonction is_same_class

Cette fonction permet de vérifier si un objet est exactement une instance de
la classe spécifiée
"""


def is_same_class(obj, a_class):
    """
    Retourne True si l'objet est une instance exacte de la classe a_class,
    sinon retourne False

    Args:
        obj (object): L'objet à vérifier.
        a_class (type): La classe à comparer

    Returns:
        bool: True si obj est une instance de a_class, False sinon
    """
    return type(obj) is a_class
