#!/usr/bin/python3
"""
Module pour la sérialisation et la désérialisation d'un dictionnaire Python en
format JSON

Ce module contient deux fonctions principales :
- serialize_and_save_to_file : Sérialise un dictionnaire Python et l'enregistre
dans un fichier JSON
- load_and_deserialize : Charge et désérialise un fichier JSON en un
dictionnaire Python
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Sérialise un dictionnaire Python et le sauvegarde dans un fichier JSON

    Args:
        data (dict): Le dictionnaire Python à sérialiser
        filename (str): Le nom du fichier JSON où les données
                        seront sauvegardées

    Returns:
        None
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Charge et désérialise les données d'un fichier JSON en dictionnaire Python

    Args:
        filename (str): Le nom du fichier JSON à charger et désérialiser

    Returns:
        dict: Le dictionnaire Python contenant les données désérialisées
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
