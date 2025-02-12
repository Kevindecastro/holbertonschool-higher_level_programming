#!/usr/bin/python3
"""
Définit une classe Student pouvant être sérialisée et désérialisée
"""


class Student:
    """
    Définit un étudiant avec les attributs first_name, last_name et age
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialise une instance de Student

        Args:
            first_name (str): Prénom de l'étudiant
            last_name (str): Nom de famille de l'étudiant
            age (int): Âge de l'étudiant
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retourne un dictionnaire représentant l'instance de Student

        Args:
            attrs (list, optionnel): Liste des noms d'attributs à récupérer
                Si None, tous les attributs sont retournés

        Returns:
            dict: Dictionnaire contenant les attributs de l'instance
        """
        if attrs is None:
            return self.__dict__
        if isinstance(attrs, list) and all(isinstance(attr, str)
                                           for attr in attrs):
            return {key: self.__dict__[key] for key in attrs
                    if key in self.__dict__}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Remplace les attributs de l'instance Student avec les valeurs du
        dictionnaire fourni

        Args:
            json (dict): Dictionnaire contenant les nouvelles valeurs
                des attributs
        """
        for key, value in json.items():
            if key in self.__dict__:
                setattr(self, key, value)
