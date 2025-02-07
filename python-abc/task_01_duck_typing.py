#!/usr/bin/env python3
"""Ce module définit une classe abstraite Shape et ses implémentations
concrètes

Le module illustre le concept des classes abstraites en Python en
définissant une classe `Shape` avec les méthodes abstraites `area()`
et `perimeter()`. Deux classes concrètes, `Circle` et `Rectangle`,
héritent de `Shape` et implémentent ces méthodes

Une fonction `shape_info()` est également fournie pour afficher
l'aire et le périmètre de toute forme respectant l'interface de Shape
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Classe abstraite représentant une forme géométrique

    Cette classe définit un modèle pour les formes géométriques en exigeant
    que les sous-classes implémentent les méthodes `area()` et `perimeter()`
    """

    @abstractmethod
    def area(self):
        """Calcule et retourne l'aire de la forme

        Cette méthode doit être implémentée par toutes les sous-classes
        """
        pass

    @abstractmethod
    def perimeter(self):
        """Calcule et retourne le périmètre de la forme

        Cette méthode doit être implémentée par toutes les sous-classes
        """
        pass


class Circle(Shape):
    """Classe représentant un cercle, héritant de la classe abstraite Shape

    Attributs :
        radius (float) : Le rayon du cercle
    """

    def __init__(self, radius):
        """Initialise une instance de Circle avec un rayon donné

        Args:
            radius (float) : Le rayon du cercle
        """
        self.radius = radius

    def area(self):
        """Calcule et retourne l'aire du cercle

        Returns:
            float : L'aire du cercle, calculée comme π * rayon²
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Calcule et retourne le périmètre (circonférence) du cercle

        Returns:
            float : Le périmètre du cercle, calculé comme 2 * π * rayon
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Classe représentant un rectangle, héritant de la classe abstraite Shape

    Attributs :
        width (float) : La largeur du rectangle
        height (float) : La hauteur du rectangle
    """

    def __init__(self, width, height):
        """Initialise une instance de Rectangle avec une largeur et
        une hauteur données

        Args:
            width (float) : La largeur du rectangle
            height (float) : La hauteur du rectangle
        """
        self.width = width
        self.height = height

    def area(self):
        """Calcule et retourne l'aire du rectangle

        Returns:
            float : L'aire du rectangle, calculée comme largeur * hauteur
        """
        return self.width * self.height

    def perimeter(self):
        """Calcule et retourne le périmètre du rectangle

        Returns:
            float : Le périmètre du rectangle, calculé
            comme 2 * (largeur + hauteur)
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Affiche l'aire et le périmètre d'une forme donnée

    Cette fonction applique le concept de duck typing en acceptant tout objet
    possédant les méthodes `area()` et `perimeter()`

    Args:
        shape (Shape) : Une instance d'une classe implémentant `area()`
        et `perimeter()`
    """
    print(f"Aire : {shape.area()}")
    print(f"Périmètre : {shape.perimeter()}")
