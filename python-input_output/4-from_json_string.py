#!/usr/bin/python3
import json

"""
Module contenant une fonction pour convertir une chaîne JSON en objet Python
"""


def from_json_string(my_str):
    """
    Convertit une chaîne JSON en un objet Python

    Args:
        my_str (str): La chaîne JSON à convertir en objet

    Returns:
        object: L'objet Python correspondant à la chaîne JSON
    """
    return json.loads(my_str)
