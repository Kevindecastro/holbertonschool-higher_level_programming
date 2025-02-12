#!/usr/bin/python3
"""
Ce module permet de charger une liste d'éléments à partir d'un fichier JSON,
d'ajouter les éléments passés en ligne de commande et de sauvegarder la liste
mise à jour dans le même fichier JSON. Si le fichier n'existe pas, il est
créé.
"""
import sys
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    """
    La fonction principale de ce module. Elle charge la liste d'éléments à
    partir d'un fichier JSON, ajoute les éléments fournis en arguments via la
    ligne de commande à cette liste, et enregistre la liste mise à jour dans
    le fichier JSON.

    Elle gère également le cas où le fichier JSON n'existe pas en initialisant
    une nouvelle liste vide.
    """
    try:
        # Tentative de chargement des éléments existants
        # à partir du fichier JSON
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        # Si le fichier n'existe pas, on initialise une liste vide
        items = []

    # On ajoute les arguments passés en ligne de commande à la liste
    items.extend(sys.argv[1:])

    # Sauvegarde de la liste mise à jour dans le fichier JSON
    save_to_json_file(items, "add_item.json")


# On exécute la fonction principale si le fichier est exécuté directement
if __name__ == "__main__":
    main()
