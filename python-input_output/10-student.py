#!/usr/bin/python3

"""Ce module définit une classe Student qui représente un étudiant
   avec ses informations"""


class Student:
    """Définir un étudiant avec ses informations principales"""

    def __init__(self, first_name, last_name, age):
        """Initialisation d'un étudiant avec son prénom, son nom et son âge"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retourne un dictionnaire représentant l'étudiant,
           avec filtrage des attributs

           Si attrs est une liste de chaînes, seuls les attributs
           contenus dans cette liste sont récupérés
           """
        if isinstance(attrs, list):
            return {attr: getattr(self, attr) for attr in attrs
                    if hasattr(self, attr)}
        return self.__dict__
