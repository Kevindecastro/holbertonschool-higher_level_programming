#!/usr/bin/python3
"""
Module contenant la classe BaseGeometry avec des méthodes de validation
"""


class BaseGeometry:
    """
    Classe représentant une base pour des objets géométriques
    """

    def area(self):
        """
        Méthode qui lève une exception pour indiquer qu'elle
        n'est pas implémentée

        Raises:
            Exception: Toujours levée avec le
            message "area() is not implemented"
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Valide que value est un entier strictement positif

        Args:
            name (str): Le nom du paramètre.
            value (int): La valeur à valider

        Raises:
            TypeError: Si value n'est pas un entier.
            ValueError: Si value est inférieur ou égal à 0
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
