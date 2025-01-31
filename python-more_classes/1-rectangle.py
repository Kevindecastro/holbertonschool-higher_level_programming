#!/usr/bin/python3
"""Définit une classe Rectangle avec des attributs width et height"""


class Rectangle:
    """Représente un rectangle"""

    def __init__(self, width=0, height=0):
        """Initialise le rectangle avec une largeur et une hauteur"""
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
