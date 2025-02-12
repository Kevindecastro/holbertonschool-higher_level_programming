#!/usr/bin/python3
"""
Module contenant une fonction pour enregistrer
un objet Python dans un fichier JSON
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Enregistre un objet Python dans un fichier sous format JSON

    Args:
        my_obj (object): L'objet Python à enregistrer
        filename (str): Le nom du fichier où enregistrer l'objet
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
