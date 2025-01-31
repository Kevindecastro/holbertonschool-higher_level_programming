#!/usr/bin/python3
"""Définit une classe Rectangle avec des méthodes __str__ et __repr__"""


class Rectangle:
    """Représente un rectangle"""

    def __init__(self, width=0, height=0):
        """Initialise le rectangle avec une largeur et une hauteur."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter pour width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter pour width"""
        if not type(value) is int:
            raise TypeError("width must be an integer")
        if int(value) < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter pour height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter pour height"""
        if not type(value) is int:
            raise TypeError("height must be an integer")
        if int(value) < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Retourne l'aire du rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Retourne le périmètre du rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Retourne une représentation en chaîne du rectangle avec des #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_str = []
        for _ in range(self.__height):
            rectangle_str.append("#" * self.__width)
        return "\n".join(rectangle_str)
