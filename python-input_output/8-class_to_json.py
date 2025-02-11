#!/usr/bin/python3
""" Module pour sérialiser un objet dans un dictionnaire
    pour JSON """


def class_to_json(obj):
    """
    Retourne un dictionnaire avec les attributs de l'objet pour
    la sérialisation JSON

    Cette fonction permet de sérialiser l'objet en récupérant
    tous les attributs publics et privés de la classe sous forme
    de dictionnaire. Les types simples comme les listes,
    dictionnaires, chaînes, entiers et booléens sont supportés
    """
    return obj.__dict__
