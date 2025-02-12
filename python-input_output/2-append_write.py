#!/usr/bin/python3
"""
Module contenant une fonction pour ajouter du texte à un fichier.
"""


def append_write(filename="", text=""):
    """
    Ajoute une chaîne de caractères à la fin d'un fichier texte (UTF8)
    et retourne le nombre de caractères ajoutés.

    Args:
        filename (str): Le nom du fichier.
        text (str): Le texte à ajouter dans le fichier.

    Returns:
        int: Nombre de caractères ajoutés.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
