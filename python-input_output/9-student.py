#!/usr/bin/python3

"""Ce module définit une classe Student qui représente un étudiant"""


class Student:
    """Définir un étudiant avec ses informations principales"""

    def __init__(self, first_name, last_name, age):
        """Initialisation d'un étudiant avec son prénom, son nom et son âge"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retourne un dictionnaire des attributs de l'objet Student"""
        return self.__dict__
