#!/usr/bin/python3
def safe_print_integer(value):
    """
    Affiche un entier de manière sécurisée.

    Args:
        value: Valeur à afficher.

    Returns:
        bool: True si l'affichage réussit, sinon False.
    """
    try:
        print("{:d}".format(value))  # Affiche la valeur si c'est un entier
        return True
    except (ValueError, TypeError):  # Gère les erreurs pour les non-entiers
        return False
