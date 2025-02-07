#!/usr/bin/python3
"""
Module contenant la classe BaseGeometry
"""


class BaseGeometry:
    """
    La classe BaseGeometry représente une géométrie de base.

    Cette classe est utilisée comme une classe de base pour d'autres formes géométriques.
    Elle définit des méthodes communes pour calculer l'aire (qui n'est pas implémentée ici)
    et pour valider les entiers dans des contextes géométriques.
    """

    def area(self):
        """
        Méthode qui soulève une exception pour indiquer que la méthode n'est pas implémentée.

        Cette méthode devrait être implémentée dans les classes filles pour calculer l'aire
        d'une forme géométrique spécifique (par exemple, un rectangle, un cercle, etc.).
        """
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """
        Valide que la valeur donnée est un entier et qu'il est supérieur à zéro.

        Args:
            name (str): Le nom de la valeur à valider.
            value (int): La valeur à valider.

        Raises:
            TypeError: Si value n'est pas un entier.
            ValueError: Si value est inférieur ou égal à zéro.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
