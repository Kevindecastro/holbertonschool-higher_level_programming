#!/usr/bin/python3

def multiple_returns(sentence):
    """
    Retourne un tuple contenant
    la longueur d'une chaîne et son premier caractère.
    Si la chaîne est vide,
    retourne un tuple avec la longueur 0 et None comme premier caractère.

    Args:
        sentence (str): La chaîne de caractères à analyser.

    Returns:
        tuple: Un tuple contenant la longueur de la chaîne
        et le premier caractère,
        ou (0, None) si la chaîne est vide.
    """
    # Vérifie si la chaîne est vide
    if sentence == "":
        # Retourne (0, None) si la chaîne est vide
        return (0, None)

    # Retourne un tuple contenant la longueur de la chaîne
    # et le premier caractère
    return (len(sentence), sentence[0])
