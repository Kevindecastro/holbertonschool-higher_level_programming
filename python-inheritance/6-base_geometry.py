#!/usr/bin/python3
"""
Module contenant la classe BaseGeometry
"""


class BaseGeometry:
    """
    Classe représentant une base pour des objets géométriques
    """

    def area(self):
        """
        Méthode qui lève une exception pour indiquer
        qu'elle n'est pas implémentée

        Raises:
            Exception: Toujours levée avec le
            message "area() is not implemented"
        """
        raise Exception("area() is not implemented")
