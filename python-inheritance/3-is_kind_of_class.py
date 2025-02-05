#!/usr/bin/python3
"""
Module contenant la fonction is_kind_of_class

Cette fonction permet de vérifier si un objet est une instance de la classe
spécifiée, ou d'une classe qui en hérite
"""


def is_kind_of_class(obj, a_class):
    """
    Retourne True si l'objet est une instance de la classe a_class, ou
    d'une de ses sous-classes, sinon retourne False

    Args:
        obj (object): L'objet à vérifier.
        a_class (type): La classe à comparer

    Returns:
        bool: True si obj est une instance de a_class ou de ses sous-classes,
              False sinon
    """
    return isinstance(obj, a_class)
