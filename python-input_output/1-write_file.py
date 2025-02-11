#!/usr/bin/python3
"""
Module contenant une fonction pour écrire dans un fichier texte
"""


def write_file(filename="", text=""):
    """
    Écrit une chaîne de caractères dans un fichier texte (UTF8)
    et retourne le nombre de caractères écrits

    Args:
        filename (str): Le nom du fichier
        text (str): Le texte à écrire dans le fichier

    Returns:
        int: Nombre de caractères écrits
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
