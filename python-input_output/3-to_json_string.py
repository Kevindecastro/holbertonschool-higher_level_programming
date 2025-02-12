#!/usr/bin/python3
""" Module contenant une fonction pour
    convertir un objet Python en chaîne JSON """
import json


def to_json_string(my_obj):
    """
    Convertit un objet Python en une chaîne JSON

    Args:
        my_obj (object): L'objet Python à convertir en JSON

    Returns:
        str: La chaîne JSON représentant l'objet
    """
    return json.dumps(my_obj)
