#!/usr/bin/python3
""" Ajoute une méthode `area()` pour calculer l'aire du carré."""


class Square:
    """ Classe représentant un carré avec un calcul de l'aire """
    def __init__(self, size=0):
        # Vérification que size est un entier
        if type(size) != int:
            raise TypeError("size must be an integer")
        # Vérification que size est positif ou égal à zéro
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size  # Initialisation de l'attribut __size

    def area(self):
        """ Retourne l'aire du carré """
        return self.__size ** 2  # L'aire est égale à la taille au carré
