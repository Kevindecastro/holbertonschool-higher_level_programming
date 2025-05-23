#!/usr/bin/python3
"""
Module contenant la classe Rectangle qui hérite de BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Classe représentant un rectangle, héritant de BaseGeometry
    """

    def __init__(self, width, height):
        """
        Initialise un rectangle avec une largeur et une hauteur

        Args:
            width (int): La largeur du rectangle
            height (int): La hauteur du rectangle

        Raises:
            TypeError: Si width ou height ne sont pas des entiers
            ValueError: Si width ou height sont <= 0
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
