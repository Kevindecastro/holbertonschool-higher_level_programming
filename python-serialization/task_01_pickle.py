#!/usr/bin/python3
"""
Module pour la sérialisation et la désérialisation d'un objet personnalisé à
l'aide du module pickle

Ce module contient la classe CustomObject, qui permet de sérialiser et
désérialiser des objets Python. Elle inclut également une méthode pour afficher
ses attributs
"""

import pickle


class CustomObject:
    """
    Classe représentant un objet personnalisé avec des attributs de base

    Attributs:
        name (str): Le nom de la personne
        age (int): L'âge de la personne
        is_student (bool): Si la personne est un étudiant

    Méthodes:
        display: Affiche les attributs de l'objet
        serialize: Sérialise l'objet dans un fichier avec pickle
        deserialize: Désérialise un objet depuis un fichier pickle
    """

    def __init__(self, name, age, is_student):
        """
        Initialisation de l'objet avec les attributs fournis

        Args:
            name (str): Le nom de la personne
            age (int): L'âge de la personne
            is_student (bool): Si la personne est un étudiant
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Affiche les attributs de l'objet

        Returns:
            None
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Sérialise l'objet dans un fichier à l'aide du module pickle

        Args:
            filename (str): Le nom du fichier dans lequel
                            l'objet sera sérialisé

        Returns:
            None
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception as e:
            print(f"Error serializing object: {e}")

    @classmethod
    def deserialize(cls, filename):
        """
        Désérialise un objet à partir d'un fichier pickle

        Args:
            filename (str): Le nom du fichier à partir duquel l'objet sera
            désérialisé

        Returns:
            CustomObject: L'objet désérialisé
            None: Si une erreur se produit pendant la désérialisation
        """
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except Exception as e:
             print(f"An error occurred while deserializing: {e}")
             return None
