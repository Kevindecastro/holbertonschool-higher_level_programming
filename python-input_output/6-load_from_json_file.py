#!/usr/bin/python3
import json

"""
Module contenant une fonction pour charger un objet
Python depuis un fichier JSON
"""


def load_from_json_file(filename):
    """
    Charge un objet Python à partir d'un fichier JSON

    Args:
        filename (str): Le nom du fichier contenant la chaîne JSON

    Returns:
        object: L'objet Python correspondant au contenu du fichier JSON
    """
    with open(filename, 'r') as file:
        return json.load(file)
