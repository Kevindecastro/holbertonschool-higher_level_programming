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

    # Enlever les espaces en début et fin de texte
    text = text.strip()

    # Vérification si le texte est vide après suppression des espaces
    if not text:
        return

    # Parcourir chaque caractère du texte
    i = 0
    while i < len(text):
        # Imprimer jusqu'au prochain caractère spécial
        if text[i] in ['.', '?', ':']:
            print(text[i], end="")  # Afficher le caractère spécial sans espace
            print()  # Imprimer une nouvelle ligne après
            print()  # Imprimer une deuxième nouvelle ligne
            i += 1  # Passer au caractère suivant
            # Sauter les espaces qui suivent la ponctuation
            while i < len(text) and text[i] == ' ':
                i += 1
        elif text[i] == ' ' and (i == 0 or text[i-1] in ['.', '?', ':']):
            # Ne pas imprimer les espaces qui suivent immédiatement
            # un caractère de ponctuation
            i += 1
        else:
            # Imprimer les caractères jusqu'à trouver un caractère spécial
            print(text[i], end="")
            i += 1
