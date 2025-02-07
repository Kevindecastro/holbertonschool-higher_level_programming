#!/usr/bin/python3
"""
Module contenant la classe Square qui hérite de Rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Classe représentant un carré, héritant de Rectangle
    """

    def __init__(self, size):
        """
        Initialise un carré avec une taille donnée

        Args:
            size (int): La taille du carré

        Raises:
            TypeError: Si size n'est pas un entier
            ValueError: Si size est <= 0
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Calcule et retourne l'aire du carré

        Returns:
            int: Aire du carré
        """
        return self.__size ** 2

    def __str__(self):
        """
        Retourne une chaîne de caractères représentant la description du carré

        Returns:
            str: Description du carré
        """
        return f"[Square] {self.__size}/{self.__size}"
