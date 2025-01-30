#!/usr/bin/python3
""" Crée une méthode `my_print()` pour
afficher un carré avec le caractère `#` """


class Square:
    """ Classe représentant un carré avec affichage de la forme """
    def __init__(self, size=0):
        self.size = size  # Utilisation du setter pour l'attribut size

    @property
    def size(self):
        """ Retourne la taille du carré """
        return self.__size

    @size.setter
    def size(self, value):
        """ Définit la taille du carré avec validation """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value  # Si validé, on définit la taille

    def my_print(self):
        """ Affiche le carré avec le caractère # """
        if self.__size == 0:
            print()  # Si la taille est 0, on affiche juste une ligne vide
        else:
            for _ in range(self.__size):  # Affichage ligne par ligne
                print("#" * self.__size)
