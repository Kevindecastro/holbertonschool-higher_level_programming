#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """
    Additionne deux tuples élément par élément.
    Si un tuple a moins de deux éléments,
    des zéros sont ajoutés pour compléter.

    Args:
        tuple_a (tuple): Le premier tuple, par défaut un tuple vide.
        tuple_b (tuple): Le deuxième tuple, par défaut un tuple vide.

    Returns:
        tuple: Un tuple contenant la somme des premiers éléments et
        des deuxièmes éléments des tuples fournis.
    """
    # Ajoute (0, 0) à tuple_a pour s'assurer qu'il a au moins deux éléments
    a = tuple_a + (0, 0)

    # Ajoute (0, 0) à tuple_b pour s'assurer qu'il a au moins deux éléments
    b = tuple_b + (0, 0)

    # Retourne un nouveau tuple avec la somme des premiers éléments
    # et la somme des deuxièmes éléments
    return (a[0] + b[0], a[1] + b[1])
