#!/usr/bin/python3
def safe_print_division(a, b):
    """
    Effectue la division de a par b en gérant les erreurs.

    Args:
        a (int, float): Numérateur.
        b (int, float): Dénominateur.

    Returns:
        float or None: Résultat de la division ou None en cas d'erreur.
    """
    try:
        result = a / b  # Effectue la division
    except ZeroDivisionError:
        result = None  # Gère la division par zéro
    finally:
        print("Inside result: {}".format(result))  # Affiche le résultat
        return result
