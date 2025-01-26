#!/usr/bin/python3
"""
Module 3-say_my_name
Définit une fonction `say_my_name` qui imprime un nom complet.
"""


def say_my_name(first_name, last_name=""):
    """
    Imprime "My name is <first_name> <last_name>".

    Arguments :
        first_name (str): Le prénom à afficher.
        last_name (str): Le nom de famille à afficher
                         (par défaut est vide).

    Exceptions :
        TypeError: Si first_name ou last_name
        n'est pas une chaîne de caractères.
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}".strip())
