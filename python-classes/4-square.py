#!/usr/bin/python3
""" Utilise une propriété pour gérer l'attribut `size`
et ses modifications """

class Square:
    """ Classe représentant un carré avec une propriété
        et un setter pour size """
    
    def __init__(self, size=0):
        self.size = size  # Utilisation du setter pour l'attribut size

    @property
    def size(self):
        """ Retourne la taille du carré """
        return self.__size

    @size.setter
    def size(self, value):
        """ Définit la taille du carré avec validation """
        # Vérification que la taille est un entier
        if type(value) != int:
            raise TypeError("size must be an integer")
        # Vérification que la taille est positive ou égale à zéro
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value  # Si validé, on définit la taille

    def area(self):
        """ Retourne l'aire du carré """
        return self.__size * self.__size  # Aire = taille * taille
