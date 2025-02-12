#!/usr/bin/python3
"""
Module contenant une fonction pour lire un fichier et afficher son contenu.
"""


def read_file(filename=""):
    """
    Lit un fichier texte (UTF8) et affiche son contenu sur la sortie standard.

    Args:
        filename (str): Le nom du fichier à lire.
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
