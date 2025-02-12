#!/usr/bin/python3
"""
Module pour la conversion de données CSV en JSON

Ce module contient une fonction pour lire les données d'un fichier CSV et les
convertir en format JSON.
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convertit un fichier CSV en un fichier JSON

    Args:
        csv_filename (str): Le nom du fichier CSV à convertir

    Returns:
        bool: True si la conversion est réussie, False en cas d'erreur
    """
    try:
        # Ouverture du fichier CSV
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            # Utilisation de DictReader pour lire chaque ligne
            # comme un dictionnaire
            csv_reader = csv.DictReader(csv_file)
            data = [row for row in csv_reader]

        # Sérialisation des données en JSON et sauvegarde dans data.json
        with open("data.json", mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file)
        return True

    except FileNotFoundError:
        print(f"Error: File {csv_filename} not found.")
        return False

    except Exception as e:
        print(f"An error occurred: {e}")
        return False
