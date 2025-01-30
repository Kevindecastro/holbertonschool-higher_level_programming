#!/usr/bin/python3
""" Ajoute un attribut privé `size` à la classe Square
pour représenter la taille du carré """


class Square:
    """ Classe représentant un carré avec un attribut size """
    def __init__(self, size):
        # Initialisation de l'attribut privé __size avec la valeur fournie
        self.__size = size
