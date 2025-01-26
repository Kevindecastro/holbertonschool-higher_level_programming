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

    # Supprimer les espaces avant et après le texte
    text = text.strip()

    i = 0
    while i < len(text):
        if text[i] in ['.', '?', ':']:
            print(text[i], end="")  # Imprimer la ponctuation
            print()  # Nouvelle ligne après la ponctuation
            # Une seule nouvelle ligne ici pour respecter la règle
            i += 1
            # Sauter les espaces qui suivent la ponctuation
            while i < len(text) and text[i] == ' ':
                i += 1
        else:
            # Imprimer le texte sans ajout d'espace en début de ligne
            print(text[i], end="")
            i += 1
