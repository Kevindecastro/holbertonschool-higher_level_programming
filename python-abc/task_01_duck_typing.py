#!/usr/bin/env python3
"""Module définissant une hiérarchie de formes géométriques
avec des méthodes pour calculer l'aire et le périmètre"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Classe abstraite représentant une forme géométrique"""

    @abstractmethod
    def area(self):
        """Retourne l'aire de la forme"""
        pass

    @abstractmethod
    def perimeter(self):
        """Retourne le périmètre de la forme"""
        pass


class Circle(Shape):
    """Classe représentant un cercle"""

    def __init__(self, radius):
        """Initialise un cercle avec un rayon donné"""
        self.radius = radius

    def area(self):
        """Calcule et retourne l'aire du cercle"""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Calcule et retourne le périmètre du cercle"""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Classe représentant un rectangle"""

    def __init__(self, width, height):
        """Initialise un rectangle avec une largeur et une hauteur"""
        self.width = width
        self.height = height

    def area(self):
        """Calcule et retourne l'aire du rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Calcule et retourne le périmètre du rectangle"""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Affiche l'aire et le périmètre d'un objet Shape"""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
