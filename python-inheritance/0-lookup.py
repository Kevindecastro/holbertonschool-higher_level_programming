#!/usr/bin/python3
"""
Module contenant la fonction lookup

Cette fonction renvoie une liste des attributs et méthodes d'un objet donné
"""


def lookup(obj):
    """
    Retourne la liste des attributs et méthodes d'un objet

    Args:
        obj (object): L'objet dont on veut connaître les attributs et méthodes

    Returns:
        list: La liste des attributs et méthodes de l'objet
    """
    return dir(obj)
