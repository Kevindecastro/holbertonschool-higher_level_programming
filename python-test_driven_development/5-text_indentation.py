#!/usr/bin/python3
"""
Imprime un texte avec deux nouvelles lignes après chaque occurrence de
'.', '?', et ':'.
"""


def text_indentation(text):
    """
    Imprime le texte avec deux nouvelles lignes après chaque '.', '?', ou ':'.

    Args:
        text (str): Le texte à imprimer.

    Raises:
        TypeError: Si 'text' n'est pas une chaîne de caractères.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Parcourir chaque caractère du texte
    i = 0
    while i < len(text):
        # Imprimer jusqu'au prochain caractère spécial
        if text[i] in ['.', '?', ':']:
            print(text[i], end="")  # Afficher le caractère spécial sans espace
            print()  # Imprimer une nouvelle ligne après
            print()  # Imprimer une deuxième nouvelle ligne
            i += 1  # Passer au caractère suivant
        elif (text[i] == ' ' and i + 1 < len(text) and
              text[i + 1] in ['.', '?', ':']):
            # Eviter les espaces avant les caractères spéciaux
            i += 1
        else:
            # Imprimer les caractères jusqu'à trouver un caractère spécial
            print(text[i], end="")
            i += 1
