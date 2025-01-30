#!/usr/bin/python3
""" Ajoute un attribut `position` pour afficher le carré avec des espaces """


class Square:
    """ Classe représentant un carré avec position et taille """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size  # Utilisation du setter pour l'attribut size
        self.position = position  # Utilisation du setter pour la position

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

    @property
    def position(self):
        """ Retourne la position du carré """
        return self.__position

    @position.setter
    def position(self, value):
        """ Définit la position du carré avec validation """
        if (len(value) != 2 or not all(isinstance(i, int) for i in value) or
                value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value  # Si validé, on définit la position

    def my_print(self):
        """Affiche le carré avec le caractère #,
           en tenant compte de la position."""
        if self.__size == 0:
            print()  # Si la taille est 0, on affiche une ligne vide
        else:
            # Affichage de la position avant de commencer à afficher le carré
            for _ in range(self.__position[1]):  # Espaces verticaux
                print()
            for _ in range(self.__size):  # Affichage ligne par ligne
                print(" " * self.__position[0] + "#" * self.__size)
