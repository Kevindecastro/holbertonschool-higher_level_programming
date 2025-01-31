#!/usr/bin/python3
"""Définit une classe Rectangle avec une méthode pour
   comparer deux rectangles"""


class Rectangle:
    """Représente un rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialise le rectangle avec une largeur et une hauteur"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        """Retourne une représentation en chaîne du
           rectangle avec le symbole"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_str = []
        for _ in range(self.__height):
            rectangle_str.append(str(self.print_symbol) * self.__width)
        return "\n".join(rectangle_str)

    def __repr__(self):
        """Retourne une chaîne pour recréer l'objet"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Affiche un message lors de la suppression de l'instance"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Retourne le plus grand rectangle en fonction de l'aire"""
        if not type(rect_1) is Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not type(rect_2) is Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
