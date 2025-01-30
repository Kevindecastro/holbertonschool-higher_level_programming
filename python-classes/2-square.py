#!/usr/bin/python3
""" Vérifie que `size` est un entier positif ou égal à zéro """


class Square:
    """ Classe représentant un carré avec une validation de size """
    def __init__(self, size=0):
        # Vérification que size est un entier
        if type(size) != int:
            raise TypeError("size must be an integer")
        # Vérification que size est un entier positif ou égal à zéro
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size  # Si validé, on initialise l'attribut __size
