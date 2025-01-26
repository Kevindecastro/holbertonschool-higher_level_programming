#!/usr/bin/python3
"""
Imprime le nom complet sous la forme "My name is <first_name> <last_name>"
"""


def say_my_name(first_name, last_name=""):
    """
    Imprime "My name is <first_name> <last_name>".

    Args:
        first_name (str): Le prénom à afficher.
        last_name (str, optionnel): Le nom de famille à afficher
                                    (vide par défaut).

    Raises:
        TypeError: Si first_name ou last_name ne sont pas des chaînes
                   de caractères.
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}".strip())
