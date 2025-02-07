#!/usr/bin/python3
"""
Module contenant la classe MyList qui hérite de la classe list
Cette classe ajoute la méthode print_sorted pour afficher la liste triée
"""


class MyList(list):
    """
    Classe héritant de la classe list et ajoutant la méthode print_sorted

    La méthode print_sorted permet d'afficher les éléments de la liste triée
    dans l'ordre croissant.
    """

    def print_sorted(self):
        """
        Affiche la liste triée en ordre croissant

        La méthode ne modifie pas la liste originale, elle imprime simplement
        les éléments triés
        """

        print(sorted(self))
